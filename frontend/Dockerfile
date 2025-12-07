FROM node:18-alpine AS build
WORKDIR /app
COPY package.json ./
COPY src ./src
RUN npm install
RUN npm run build


FROM docker.io/nginx:stable-alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
