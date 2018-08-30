FROM nginx:alpine

WORKDIR /

RUN apk update && apk upgrade && rm /etc/nginx/conf.d/*.conf && rm /var/cache/apk/*

COPY conf.d/ /etc/nginx/conf.d/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]