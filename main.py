import os

import click
import uvicorn

from app.core.utils.logger import get_logger

logger = get_logger(__name__)


@click.command()
@click.option(
    "--env",
    type=click.Choice(["dev", "prd"], case_sensitive=False),
    default="dev",
)
def main(env:str):

    os.environ["ENV"] = env
    uvicorn.run(
        app="app.server:app",
        host="0.0.0.0",
        port=3030 if env == 'prd' else 3080,
        reload=True if env != "prd" else False,
        workers=1,
    )


if __name__ == "__main__":   
    main()
