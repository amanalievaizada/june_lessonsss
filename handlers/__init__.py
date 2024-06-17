from aiogram import Router


def setup_routers() -> Router:
    from . import (
        start,
        registration,
        profile,
        like_dislike,
    )

    router = Router()

    router.include_router(start.router)
    router.include_router(registration.router)
    router.include_router(profile.router)
    router.include_router(like_dislike.router)

    return router
