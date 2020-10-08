FROM node:carbon-slim

# Create app directory
WORKDIR /categories_api

# Install app dependencies
COPY package.json /categories_api/
RUN npm install

# Bundle app source
COPY . /categories_api/
RUN npm run prepublish

CMD [ "npm", "run", "runServer" ]
