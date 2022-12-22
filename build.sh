docker build -f Dockerfile.base -t hw3helper_bot_base:latest .
docker build -f Dockerfile.bot -t hw3helper_bot_bot:latest .
docker build -f Dockerfile.db -t hw3helper_bot_db:latest .
