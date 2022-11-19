FROM nginx:1.15.12 AS base

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.template /etc/nginx/nginx.template

EXPOSE 80

EXPOSE 443