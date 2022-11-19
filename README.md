# Football WebSite API 

This is a simple API for football website. 
It is a REST API that provides data about football matches, teams, players, etc.
It can be customized for use in any football website.

## Installation

1. Clone the repository
2. Run `make install` to install the dependencies
3. Run `make run` to run the server

## Usage

The API is available at `http://localhost:8000/api/v1/`

## Endpoints

### Matches

- `GET /matches/` - Get all matches
- `GET /matches/<id>/` - Get a match by id
- `POST /matches/` - Create a new match
- `PUT /matches/<id>/` - Update a match
- `DELETE /matches/<id>/` - Delete a match

### Teams

- `GET /clubs/` - Get all teams
- `GET /clubs/<id>/` - Get a team by id
- `POST /clubs/` - Create a new team
- `PUT /clubs/<id>/` - Update a team
- `DELETE /clubs/<id>/` - Delete a team


### Players

- `GET /players/` - Get all players
- `GET /players/<id>/` - Get a player by id
- `POST /players/` - Create a new player
- `PUT /players/<id>/` - Update a player
- `DELETE /players/<id>/` - Delete a player


### CMS

- `GET /cms/` - Get all CMS pages
- `GET /cms/<id>/` - Get a CMS page by id
- `POST /cms/` - Create a new CMS page
- `PUT /cms/<id>/` - Update a CMS page
- `DELETE /cms/<id>/` - Delete a CMS page


### News

- `GET /news/` - Get all news
- `GET /news/<id>/` - Get a news by id
- `POST /news/` - Create a new news
- `PUT /news/<id>/` - Update a news
- `DELETE /news/<id>/` - Delete a news

