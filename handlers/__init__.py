from aiogram import Router


def setup_routers() -> Router:
    from . import (
        start,
        registration,
        profile,
        like_dislike,
        reference,
        donate,
    )

    router = Router()

    router.include_router(start.router)
    router.include_router(registration.router)
    router.include_router(profile.router)
    router.include_router(like_dislike.router)
    router.include_router(reference.router)
    router.include_router(donate.router)

    return router
