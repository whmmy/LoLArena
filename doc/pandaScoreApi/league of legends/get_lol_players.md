> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List LoL players

List players for the League of Legends videogame
> ℹ️  
> 
> This endpoint is available to all customers

# OpenAPI definition

```json
{
  "components": {
    "parameters": {
      "Page": {
        "description": "Pagination in the form of `page=2` or `page[size]=30&page[number]=2`",
        "in": "query",
        "name": "page",
        "required": false,
        "schema": {
          "oneOf": [
            {
              "default": 1,
              "minimum": 1,
              "type": "integer"
            },
            {
              "additionalProperties": false,
              "properties": {
                "number": {
                  "default": 1,
                  "minimum": 1,
                  "type": "integer"
                },
                "size": {
                  "default": 50,
                  "maximum": 100,
                  "minimum": 1,
                  "type": "integer"
                }
              },
              "type": "object"
            }
          ]
        }
      },
      "PerPage": {
        "description": "Equivalent to `page[size]`",
        "example": 5,
        "in": "query",
        "name": "per_page",
        "required": false,
        "schema": {
          "default": 50,
          "maximum": 100,
          "minimum": 1,
          "type": "integer"
        }
      }
    },
    "responses": {
      "Error400": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Bad request"
      },
      "Error401": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Unauthorized"
      },
      "Error403": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Forbidden"
      },
      "Error404": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Not found"
      },
      "Error422": {
        "content": {
          "application/json": {
            "schema": {
              "properties": {
                "error": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          }
        },
        "description": "Unprocessable Entity"
      },
      "LoLPlayers": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/players?page[size]=1": {
                "description": "/lol/players?page[size]=1",
                "value": [
                  {
                    "active": true,
                    "age": 26,
                    "birthday": "1999-03-08",
                    "current_team": {
                      "acronym": "GP",
                      "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/137375/600px_galions_darkmode.png",
                      "id": 137375,
                      "image_url": "https://cdn.pandascore.co/images/team/image/137375/600px_galions_lightmode.png",
                      "location": "FR",
                      "modified_at": "2025-10-05T06:08:10Z",
                      "name": "Galions Pearl",
                      "slug": "galions-pearl"
                    },
                    "current_videogame": {
                      "id": 1,
                      "name": "LoL",
                      "slug": "league-of-legends"
                    },
                    "first_name": "Vildan",
                    "id": 62082,
                    "image_url": null,
                    "last_name": "Soylu",
                    "modified_at": "2025-10-05T06:08:25Z",
                    "name": "Telch",
                    "nationality": "TR",
                    "role": "top",
                    "slug": "telch"
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLPlayers"
            }
          }
        },
        "description": "A list of League-of-Legends players"
      }
    },
    "schemas": {
      "LoLPlayers": {
        "items": {
          "additionalProperties": false,
          "deprecated": false,
          "properties": {
            "active": {
              "description": "Whether player is active",
              "title": "PlayerIsActive",
              "type": "boolean"
            },
            "age": {
              "deprecated": false,
              "description": "Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age)\n**Note**: This field is only present for users running the Historical plan or above.",
              "minimum": 0,
              "nullable": true,
              "title": "PlayerAge",
              "type": "number"
            },
            "birthday": {
              "deprecated": false,
              "description": "Birth day of the player, `YYYY-MM-DD` format. `null` if unknown.\n**Note**: This field is only present for users running the Historical plan or above.",
              "nullable": true,
              "title": "PlayerBirthday",
              "type": "string"
            },
            "current_team": {
              "additionalProperties": false,
              "deprecated": false,
              "nullable": true,
              "properties": {
                "acronym": {
                  "deprecated": false,
                  "nullable": true,
                  "title": "TeamAcronym",
                  "type": "string"
                },
                "dark_mode_image_url": {
                  "deprecated": false,
                  "description": "URL of the team logo",
                  "format": "uri",
                  "nullable": true,
                  "title": "TeamImageURL",
                  "type": "string"
                },
                "id": {
                  "description": "The ID of the team.",
                  "minimum": 1,
                  "title": "TeamID",
                  "type": "integer"
                },
                "image_url": {
                  "deprecated": false,
                  "description": "URL of the team logo",
                  "format": "uri",
                  "nullable": true,
                  "title": "TeamImageURL",
                  "type": "string"
                },
                "location": {
                  "deprecated": false,
                  "description": "The team's organization location",
                  "nullable": true,
                  "title": "TeamLocation",
                  "type": "string"
                },
                "modified_at": {
                  "format": "date-time",
                  "minLength": 1,
                  "title": "TeamModifiedAt",
                  "type": "string"
                },
                "name": {
                  "description": "The name of the team.",
                  "title": "TeamName",
                  "type": "string"
                },
                "slug": {
                  "deprecated": false,
                  "minLength": 1,
                  "nullable": true,
                  "pattern": "^[a-z0-9_-]+$",
                  "title": "TeamSlug",
                  "type": "string"
                }
              },
              "required": [
                "acronym",
                "dark_mode_image_url",
                "id",
                "image_url",
                "location",
                "modified_at",
                "name",
                "slug"
              ],
              "title": "BaseTeam",
              "type": "object"
            },
            "current_videogame": {
              "deprecated": false,
              "enum": [
                {
                  "id": 1,
                  "name": "LoL",
                  "slug": "league-of-legends"
                },
                {
                  "id": 3,
                  "name": "Counter-Strike",
                  "slug": "cs-go"
                },
                {
                  "id": 4,
                  "name": "Dota 2",
                  "slug": "dota-2"
                },
                {
                  "id": 14,
                  "name": "Overwatch",
                  "slug": "ow"
                },
                {
                  "id": 20,
                  "name": "PUBG",
                  "slug": "pubg"
                },
                {
                  "id": 22,
                  "name": "Rocket League",
                  "slug": "rl"
                },
                {
                  "id": 23,
                  "name": "Call of Duty",
                  "slug": "cod-mw"
                },
                {
                  "id": 24,
                  "name": "Rainbow 6 Siege",
                  "slug": "r6-siege"
                },
                {
                  "id": 25,
                  "name": "EA Sports FC",
                  "slug": "fifa"
                },
                {
                  "id": 26,
                  "name": "Valorant",
                  "slug": "valorant"
                },
                {
                  "id": 27,
                  "name": "King of Glory",
                  "slug": "kog"
                },
                {
                  "id": 28,
                  "name": "LoL Wild Rift",
                  "slug": "lol-wild-rift"
                },
                {
                  "id": 29,
                  "name": "StarCraft 2",
                  "slug": "starcraft-2"
                },
                {
                  "id": 30,
                  "name": "StarCraft Brood War",
                  "slug": "starcraft-brood-war"
                },
                {
                  "id": 31,
                  "name": "eSoccer",
                  "slug": "e-soccer"
                },
                {
                  "id": 32,
                  "name": "eBasketball",
                  "slug": "e-basketball"
                },
                {
                  "id": 33,
                  "name": "eCricket",
                  "slug": "e-cricket"
                },
                {
                  "id": 34,
                  "name": "Mobile Legends: Bang Bang",
                  "slug": "mlbb"
                },
                {
                  "id": 35,
                  "name": "eHockey",
                  "slug": "e-hockey"
                },
                {
                  "id": 36,
                  "name": "eTennis",
                  "slug": "e-tennis"
                }
              ],
              "nullable": true,
              "title": "CurrentVideogame",
              "type": "object"
            },
            "first_name": {
              "deprecated": false,
              "description": "First name of the player. `null` if unknown",
              "nullable": true,
              "title": "PlayerFirstName",
              "type": "string"
            },
            "id": {
              "description": "ID of the player",
              "minimum": 1,
              "title": "PlayerID",
              "type": "integer"
            },
            "image_url": {
              "deprecated": false,
              "description": "URL to the photo of the player. `null` if not available.",
              "format": "uri",
              "nullable": true,
              "title": "PlayerImageURL",
              "type": "string"
            },
            "last_name": {
              "deprecated": false,
              "description": "Last name of the player. `null` if unknown",
              "nullable": true,
              "title": "PlayerLastName",
              "type": "string"
            },
            "modified_at": {
              "format": "date-time",
              "minLength": 1,
              "title": "PlayerModifiedAt",
              "type": "string"
            },
            "name": {
              "description": "Professional name of the player",
              "title": "PlayerName",
              "type": "string"
            },
            "nationality": {
              "deprecated": false,
              "description": "Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code).\nIn addition to the standard, the `XK` code is used for Kosovo.\n`null` if unknown",
              "nullable": true,
              "title": "PlayerNationality",
              "type": "string"
            },
            "role": {
              "deprecated": false,
              "description": "Role/position of the player. Field value varies depending on the video game.`null` if unknown.\n**Note**: role is only available for DotA 2, League of Legends, and Overwatch players.\n`null` for other video games.",
              "nullable": true,
              "title": "PlayerRoleSlug",
              "type": "string"
            },
            "slug": {
              "deprecated": false,
              "description": "Unique, human-readable identifier for the player.\n`id` and `slug` can be used interchangeably throughout the API.",
              "minLength": 1,
              "nullable": true,
              "pattern": "^[a-z0-9_-]+$",
              "title": "PlayerSlug",
              "type": "string"
            }
          },
          "required": [
            "active",
            "current_team",
            "current_videogame",
            "first_name",
            "id",
            "image_url",
            "last_name",
            "modified_at",
            "name",
            "nationality",
            "role",
            "slug"
          ],
          "title": "Player",
          "type": "object"
        },
        "title": "LoLPlayers",
        "type": "array"
      },
      "filter_over_LoLPlayers": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "active": {
            "description": "Whether player is active",
            "title": "PlayerIsActive",
            "type": "boolean"
          },
          "birthday": {
            "items": {
              "description": "Birth day of the player, `YYYY-MM-DD` format. `null` if unknown.\n**Note**: This field is only present for users running the Historical plan or above.",
              "title": "PlayerBirthday",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "first_name": {
            "items": {
              "description": "First name of the player. `null` if unknown",
              "title": "PlayerFirstName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "id": {
            "items": {
              "description": "ID of the player",
              "minimum": 1,
              "title": "PlayerID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "last_name": {
            "items": {
              "description": "Last name of the player. `null` if unknown",
              "title": "PlayerLastName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "PlayerModifiedAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "description": "Professional name of the player",
              "title": "PlayerName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "nationality": {
            "items": {
              "description": "Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code).\nIn addition to the standard, the `XK` code is used for Kosovo.\n`null` if unknown",
              "title": "PlayerNationality",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "role": {
            "items": {
              "description": "Role/position of the player. Field value varies depending on the video game.`null` if unknown.\n**Note**: role is only available for DotA 2, League of Legends, and Overwatch players.\n`null` for other video games.",
              "title": "PlayerRoleSlug",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "slug": {
            "items": {
              "description": "Unique, human-readable identifier for the player.\n`id` and `slug` can be used interchangeably throughout the API.",
              "minLength": 1,
              "pattern": "^[a-z0-9_-]+$",
              "title": "PlayerSlug",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "team_id": {
            "items": {
              "description": "The ID of the team.",
              "minimum": 1,
              "title": "TeamID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "videogame_id": {
            "items": {
              "description": "A videogame ID",
              "enum": [
                1,
                3,
                4,
                14,
                20,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
                32,
                33,
                34,
                35,
                36
              ],
              "title": "VideogameID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          }
        },
        "type": "object"
      },
      "range_over_LoLPlayers": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "birthday": {
            "items": {
              "description": "Birth day of the player, `YYYY-MM-DD` format. `null` if unknown.\n**Note**: This field is only present for users running the Historical plan or above.",
              "title": "PlayerBirthday",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "first_name": {
            "items": {
              "description": "First name of the player. `null` if unknown",
              "title": "PlayerFirstName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "id": {
            "items": {
              "description": "ID of the player",
              "minimum": 1,
              "title": "PlayerID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "last_name": {
            "items": {
              "description": "Last name of the player. `null` if unknown",
              "title": "PlayerLastName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "PlayerModifiedAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "description": "Professional name of the player",
              "title": "PlayerName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "nationality": {
            "items": {
              "description": "Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code).\nIn addition to the standard, the `XK` code is used for Kosovo.\n`null` if unknown",
              "title": "PlayerNationality",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "role": {
            "items": {
              "description": "Role/position of the player. Field value varies depending on the video game.`null` if unknown.\n**Note**: role is only available for DotA 2, League of Legends, and Overwatch players.\n`null` for other video games.",
              "title": "PlayerRoleSlug",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "slug": {
            "items": {
              "description": "Unique, human-readable identifier for the player.\n`id` and `slug` can be used interchangeably throughout the API.",
              "minLength": 1,
              "pattern": "^[a-z0-9_-]+$",
              "title": "PlayerSlug",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLPlayers": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "birthday": {
            "description": "Birth day of the player, `YYYY-MM-DD` format. `null` if unknown.\n**Note**: This field is only present for users running the Historical plan or above.",
            "title": "PlayerBirthday",
            "type": "string"
          },
          "first_name": {
            "description": "First name of the player. `null` if unknown",
            "title": "PlayerFirstName",
            "type": "string"
          },
          "last_name": {
            "description": "Last name of the player. `null` if unknown",
            "title": "PlayerLastName",
            "type": "string"
          },
          "name": {
            "description": "Professional name of the player",
            "title": "PlayerName",
            "type": "string"
          },
          "nationality": {
            "description": "Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code).\nIn addition to the standard, the `XK` code is used for Kosovo.\n`null` if unknown",
            "title": "PlayerNationality",
            "type": "string"
          },
          "role": {
            "description": "Role/position of the player. Field value varies depending on the video game.`null` if unknown.\n**Note**: role is only available for DotA 2, League of Legends, and Overwatch players.\n`null` for other video games.",
            "title": "PlayerRoleSlug",
            "type": "string"
          },
          "slug": {
            "description": "Unique, human-readable identifier for the player.\n`id` and `slug` can be used interchangeably throughout the API.",
            "minLength": 1,
            "pattern": "^[a-z0-9_-]+$",
            "title": "PlayerSlug",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLPlayers": {
        "items": {
          "enum": [
            "birthday",
            "-birthday",
            "first_name",
            "-first_name",
            "id",
            "-id",
            "last_name",
            "-last_name",
            "modified_at",
            "-modified_at",
            "name",
            "-name",
            "nationality",
            "-nationality",
            "role",
            "-role",
            "slug",
            "-slug",
            "videogame_id",
            "-videogame_id",
            "team_id",
            "-team_id"
          ]
        },
        "minItems": 1,
        "type": "array"
      }
    },
    "securitySchemes": {
      "BearerToken": {
        "scheme": "bearer",
        "type": "http"
      },
      "QueryToken": {
        "in": "query",
        "name": "token",
        "type": "apiKey"
      }
    }
  },
  "info": {
    "title": "League of Legends",
    "version": "2.62.8"
  },
  "openapi": "3.0.0",
  "paths": {
    "/lol/players": {
      "get": {
        "description": "List players for the League of Legends videogame\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_players",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLPlayers"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to select results within ranges\nFor more information on ranges, see [docs](/docs/filtering-and-sorting#range).",
            "explode": true,
            "in": "query",
            "name": "range",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/range_over_LoLPlayers"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLPlayers"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLPlayers"
            },
            "style": "deepObject"
          },
          {
            "$ref": "#/components/parameters/Page"
          },
          {
            "$ref": "#/components/parameters/PerPage"
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLPlayers"
          },
          "400": {
            "$ref": "#/components/responses/Error400"
          },
          "401": {
            "$ref": "#/components/responses/Error401"
          },
          "403": {
            "$ref": "#/components/responses/Error403"
          },
          "404": {
            "$ref": "#/components/responses/Error404"
          },
          "422": {
            "$ref": "#/components/responses/Error422"
          }
        },
        "summary": "List LoL players",
        "tags": [
          "LoL players"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/players' \\\n     --header 'accept: application/json'\n",
              "language": "curl"
            }
          ]
        }
      }
    }
  },
  "security": [
    {
      "BearerToken": []
    },
    {
      "QueryToken": []
    }
  ],
  "servers": [
    {
      "url": "https://api.pandascore.co/",
      "variables": {}
    }
  ],
  "x-readme": {
    "explorer-enabled": false,
    "samples-languages": [
      "curl"
    ]
  }
}
```