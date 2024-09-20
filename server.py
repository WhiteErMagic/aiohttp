from flask import jsonify
from sqlalchemy.ext.asyncio import AsyncSession

from models import Advertisements, Session, User, init_orm, engine
from aiohttp import web

app = web.Application()


async def get_advertisement_by_id(id: int, session: AsyncSession):
    advertisement = await session.get(Advertisements, id)
    # if advertisement is None:
    #     raise get_http_error(web.HTTPNotFound, 'advertisement not found')
    return advertisement


class AdvertisementsView(web.View):

    @property
    def id(self):
        return int(self.request.match_info['id'])

    async def post(self):
        json_data = await self.request.json()
        advertisement = Advertisements(**json_data)
        self.request.session.add(advertisement)
        await self.request.session.commit()
        return web.json_response({'id': advertisement.id})

    async def patch(self):
        json_data = await self.request.json()
        advertisement = await self.request.session.get(Advertisements, self.id)
        for k, v in json_data.items():
            setattr(advertisement, k, v)
        await self.request.session.commit()
        return web.json_response({'id': advertisement.id})

    async def delete(self):
        advertisement = await self.request.session.get(Advertisements, self.id)
        await self.request.session.delete(advertisement)
        await self.request.session.commit()
        return web.json_response({'id': 'deleted'})

    async def get(self):
        advertisement = await get_advertisement_by_id(self.id, self.request.session)
        return web.json_response(advertisement.json)


app.add_routes([
    web.post("/advertisement/", AdvertisementsView),
    web.patch("/advertisement/{id}", AdvertisementsView),
    web.delete("/advertisement/{id}", AdvertisementsView),
    web.get("/advertisement/{id}", AdvertisementsView)
])


async def orm_context(app):
    print('Start')
    await init_orm()
    yield
    await engine.dispose()
    print('Stop')


@web.middleware
async def session_middleware(request: web.Request, handler):
    async with Session() as session:
        request.session = session
        response = await handler(request)
        return response

app.cleanup_ctx.append(orm_context)
app.middlewares.append(session_middleware)

web.run_app(app, host='127.0.0.1', port=8080)

