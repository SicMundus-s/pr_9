# syntax=docker/dockerfile:1

FROM node:12.18.1
WORKDIR /code/app
ENV NODE_ENV=production
COPY ./app /code/app

RUN npm install
EXPOSE 4500
CMD npm run dev