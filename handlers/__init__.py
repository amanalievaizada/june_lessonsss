from aiogram import Router


def setup_routers() -> Router:
    from . import (
        start,
        registration,
    )

    router = Router()

    router.include_router(start.router)
    router.include_router(registration.router)

    return router
