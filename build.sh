docker build -t Dockerfile.base -f hw3helper_bot_base:latest
docker build -t Dockerfile.bot -f hw3helper_bot_bot:latest
docker build -t Dockerfile.db -f hw3helper_bot_db:latest
