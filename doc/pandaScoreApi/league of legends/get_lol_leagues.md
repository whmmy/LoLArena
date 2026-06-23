> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get LoL leagues

List League of Legends leagues
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
      "LoLLeagues": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/leagues?page[size]=1": {
                "description": "/lol/leagues?page[size]=1",
                "value": [
                  {
                    "id": 4864,
                    "image_url": "https://cdn.pandascore.co/images/league/image/4864/asci_2022_logo-png",
                    "modified_at": "2022-09-07T13:38:42Z",
                    "name": "Asia Star Challengers Invitational",
                    "series": [
                      {
                        "begin_at": "2022-09-11T22:00:00Z",
                        "end_at": "2022-09-25T12:33:00Z",
                        "full_name": "2022",
                        "id": 5047,
                        "league_id": 4864,
                        "modified_at": "2022-09-25T14:51:12Z",
                        "name": "",
                        "season": null,
                        "slug": "league-of-legends-asia-star-challengers-invitational-2022",
                        "winner_id": 3457,
                        "winner_type": "Team",
                        "year": 2022
                      }
                    ],
                    "slug": "league-of-legends-asia-star-challengers-invitational",
                    "url": null,
                    "videogame": {
                      "current_version": "12.18.1",
                      "id": 1,
                      "name": "LoL",
                      "slug": "league-of-legends"
                    }
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLLeagues"
            }
          }
        },
        "description": "A list of League-of-Legends leagues"
      }
    },
    "schemas": {
      "LoLLeagues": {
        "items": {
          "additionalProperties": false,
          "deprecated": false,
          "properties": {
            "id": {
              "minimum": 1,
              "title": "LeagueID",
              "type": "integer"
            },
            "image_url": {
              "deprecated": false,
              "format": "uri",
              "nullable": true,
              "title": "LeagueImageURL",
              "type": "string"
            },
            "modified_at": {
              "format": "date-time",
              "minLength": 1,
              "title": "LeagueModifiedAt",
              "type": "string"
            },
            "name": {
              "title": "LeagueName",
              "type": "string"
            },
            "series": {
              "items": {
                "additionalProperties": false,
                "deprecated": false,
                "properties": {
                  "begin_at": {
                    "deprecated": false,
                    "format": "date-time",
                    "minLength": 1,
                    "nullable": true,
                    "title": "SerieBeginAt",
                    "type": "string"
                  },
                  "end_at": {
                    "deprecated": false,
                    "format": "date-time",
                    "minLength": 1,
                    "nullable": true,
                    "title": "SerieEndAt",
                    "type": "string"
                  },
                  "full_name": {
                    "title": "SerieFullName",
                    "type": "string"
                  },
                  "id": {
                    "minimum": 1,
                    "title": "SerieID",
                    "type": "integer"
                  },
                  "league_id": {
                    "minimum": 1,
                    "title": "LeagueID",
                    "type": "integer"
                  },
                  "modified_at": {
                    "format": "date-time",
                    "minLength": 1,
                    "title": "SerieModifiedAt",
                    "type": "string"
                  },
                  "name": {
                    "deprecated": false,
                    "nullable": true,
                    "title": "SerieName",
                    "type": "string"
                  },
                  "season": {
                    "deprecated": false,
                    "nullable": true,
                    "title": "SerieSeason",
                    "type": "string"
                  },
                  "slug": {
                    "minLength": 1,
                    "pattern": "^[a-z0-9_-]+$",
                    "title": "SerieSlug",
                    "type": "string"
                  },
                  "winner_id": {
                    "anyOf": [
                      {
                        "description": "ID of the player",
                        "minimum": 1,
                        "title": "PlayerID",
                        "type": "integer"
                      },
                      {
                        "description": "The ID of the team.",
                        "minimum": 1,
                        "title": "TeamID",
                        "type": "integer"
                      }
                    ],
                    "deprecated": false,
                    "nullable": true,
                    "title": "OpponentID"
                  },
                  "winner_type": {
                    "deprecated": false,
                    "enum": [
                      "Player",
                      "Team"
                    ],
                    "nullable": true,
                    "title": "OpponentType",
                    "type": "string"
                  },
                  "year": {
                    "deprecated": false,
                    "minimum": 2012,
                    "nullable": true,
                    "title": "SerieYear",
                    "type": "integer"
                  }
                },
                "required": [
                  "begin_at",
                  "end_at",
                  "full_name",
                  "id",
                  "league_id",
                  "modified_at",
                  "name",
                  "season",
                  "slug",
                  "winner_id",
                  "winner_type",
                  "year"
                ],
                "title": "BaseSerie",
                "type": "object"
              },
              "title": "BaseSeries",
              "type": "array"
            },
            "slug": {
              "minLength": 1,
              "pattern": "^[a-z0-9:_-]+$",
              "title": "LeagueSlug",
              "type": "string"
            },
            "url": {
              "deprecated": false,
              "format": "uri",
              "nullable": true,
              "title": "LeagueURL",
              "type": "string"
            },
            "videogame": {
              "oneOf": [
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        1
                      ]
                    },
                    "name": {
                      "enum": [
                        "LoL"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "league-of-legends"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_LoL",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        3
                      ]
                    },
                    "name": {
                      "enum": [
                        "Counter-Strike"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "cs-go"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_CSGO",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        4
                      ]
                    },
                    "name": {
                      "enum": [
                        "Dota 2"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "dota-2"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_Dota2",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        14
                      ]
                    },
                    "name": {
                      "enum": [
                        "Overwatch"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "ow"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_Overwatch",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        20
                      ]
                    },
                    "name": {
                      "enum": [
                        "PUBG"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "pubg"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_PUBG",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        22
                      ]
                    },
                    "name": {
                      "enum": [
                        "Rocket League"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "rl"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_RocketLeague",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        23
                      ]
                    },
                    "name": {
                      "enum": [
                        "Call of Duty"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "cod-mw"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_Codmw",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        24
                      ]
                    },
                    "name": {
                      "enum": [
                        "Rainbow 6 Siege"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "r6-siege"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_R6siege",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        25
                      ]
                    },
                    "name": {
                      "enum": [
                        "EA Sports FC"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "fifa"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_Fifa",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        26
                      ]
                    },
                    "name": {
                      "enum": [
                        "Valorant"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "valorant"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_Valorant",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        27
                      ]
                    },
                    "name": {
                      "enum": [
                        "King of Glory"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "kog"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_Kog",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        28
                      ]
                    },
                    "name": {
                      "enum": [
                        "LoL Wild Rift"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "lol-wild-rift"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_LolWildRift",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        29
                      ]
                    },
                    "name": {
                      "enum": [
                        "StarCraft 2"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "starcraft-2"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_Starcraft2",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        30
                      ]
                    },
                    "name": {
                      "enum": [
                        "StarCraft Brood War"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "starcraft-brood-war"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_StarcraftBroodWar",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        34
                      ]
                    },
                    "name": {
                      "enum": [
                        "Mobile Legends: Bang Bang"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "mlbb"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_MLBB",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        32
                      ]
                    },
                    "name": {
                      "enum": [
                        "eBasketball"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "e-basketball"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_EBasketball",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        33
                      ]
                    },
                    "name": {
                      "enum": [
                        "eCricket"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "e-cricket"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_ECricket",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        35
                      ]
                    },
                    "name": {
                      "enum": [
                        "eHockey"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "e-hockey"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_EHockey",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        31
                      ]
                    },
                    "name": {
                      "enum": [
                        "eSoccer"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "e-soccer"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_ESoccer",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "current_version": {
                      "deprecated": false,
                      "nullable": true,
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "id": {
                      "enum": [
                        36
                      ]
                    },
                    "name": {
                      "enum": [
                        "eTennis"
                      ]
                    },
                    "slug": {
                      "enum": [
                        "e-tennis"
                      ]
                    }
                  },
                  "required": [
                    "current_version",
                    "id",
                    "name",
                    "slug"
                  ],
                  "title": "LeagueVideogame_ETennis",
                  "type": "object"
                }
              ],
              "title": "LeagueVideogame"
            }
          },
          "required": [
            "id",
            "image_url",
            "modified_at",
            "name",
            "series",
            "slug",
            "url",
            "videogame"
          ],
          "title": "League",
          "type": "object"
        },
        "title": "LoLLeagues",
        "type": "array"
      },
      "filter_over_LoLLeagues": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "id": {
            "items": {
              "minimum": 1,
              "title": "LeagueID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "LeagueModifiedAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "LeagueName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "slug": {
            "items": {
              "minLength": 1,
              "pattern": "^[a-z0-9:_-]+$",
              "title": "LeagueSlug",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "url": {
            "items": {
              "format": "uri",
              "title": "LeagueURL",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          }
        },
        "type": "object"
      },
      "range_over_LoLLeagues": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "id": {
            "items": {
              "minimum": 1,
              "title": "LeagueID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "LeagueModifiedAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "LeagueName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "slug": {
            "items": {
              "minLength": 1,
              "pattern": "^[a-z0-9:_-]+$",
              "title": "LeagueSlug",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "url": {
            "items": {
              "format": "uri",
              "title": "LeagueURL",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLLeagues": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "name": {
            "title": "LeagueName",
            "type": "string"
          },
          "slug": {
            "minLength": 1,
            "pattern": "^[a-z0-9:_-]+$",
            "title": "LeagueSlug",
            "type": "string"
          },
          "url": {
            "format": "uri",
            "title": "LeagueURL",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLLeagues": {
        "items": {
          "enum": [
            "id",
            "-id",
            "modified_at",
            "-modified_at",
            "name",
            "-name",
            "slug",
            "-slug",
            "url",
            "-url"
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
    "/lol/leagues": {
      "get": {
        "description": "List League of Legends leagues\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_leagues",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLLeagues"
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
              "$ref": "#/components/schemas/range_over_LoLLeagues"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLLeagues"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLLeagues"
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
            "$ref": "#/components/responses/LoLLeagues"
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
        "summary": "Get LoL leagues",
        "tags": [
          "LoL leagues"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/leagues' \\\n     --header 'accept: application/json'\n",
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