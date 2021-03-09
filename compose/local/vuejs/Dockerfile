FROM node:carbon

WORKDIR /frontend

COPY ./frontend /frontend
EXPOSE 8080

RUN npm install

COPY ./compose/local/vuejs/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

CMD ["npm", "run", "dev"]

