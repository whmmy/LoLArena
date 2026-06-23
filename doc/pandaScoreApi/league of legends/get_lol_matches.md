> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# List LoL matches

List matches for the League of Legends videogame
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
      "LoLMatches": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/matches?page[size]=1": {
                "description": "/lol/matches?page[size]=1",
                "value": [
                  {
                    "begin_at": "2026-03-14T16:02:14Z",
                    "detailed_stats": true,
                    "draw": false,
                    "end_at": "2026-03-14T18:32:53Z",
                    "forfeit": false,
                    "game_advantage": null,
                    "games": [
                      {
                        "begin_at": "2026-03-14T16:02:14Z",
                        "complete": true,
                        "detailed_stats": true,
                        "end_at": "2026-03-14T16:47:56Z",
                        "finished": true,
                        "forfeit": false,
                        "id": 276434,
                        "length": 2251,
                        "match_id": 1397580,
                        "position": 1,
                        "status": "finished",
                        "winner": {
                          "id": 126215,
                          "type": "Team"
                        },
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-14T17:01:12Z",
                        "complete": true,
                        "detailed_stats": true,
                        "end_at": "2026-03-14T17:48:53Z",
                        "finished": true,
                        "forfeit": false,
                        "id": 276435,
                        "length": 2330,
                        "match_id": 1397580,
                        "position": 2,
                        "status": "finished",
                        "winner": {
                          "id": 126832,
                          "type": "Team"
                        },
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2026-03-14T17:59:14Z",
                        "complete": true,
                        "detailed_stats": true,
                        "end_at": "2026-03-14T18:32:54Z",
                        "finished": true,
                        "forfeit": false,
                        "id": 276436,
                        "length": 1497,
                        "match_id": 1397580,
                        "position": 3,
                        "status": "finished",
                        "winner": {
                          "id": 126832,
                          "type": "Team"
                        },
                        "winner_type": "Team"
                      }
                    ],
                    "id": 1397580,
                    "league": {
                      "id": 4996,
                      "image_url": "https://cdn-api.pandascore.co/images/league/image/4996/emea_masters_2023-png",
                      "modified_at": "2023-04-01T08:10:00Z",
                      "name": "EMEA Masters",
                      "slug": "league-of-legends-emea-masters",
                      "url": null
                    },
                    "league_id": 4996,
                    "live": {
                      "opens_at": null,
                      "supported": false,
                      "url": null
                    },
                    "low_latency_feed": {
                      "opens_at": null,
                      "supported": false,
                      "url": null
                    },
                    "match_type": "best_of",
                    "modified_at": "2026-03-14T19:11:46Z",
                    "name": "Lower bracket final: WLG vs USE",
                    "number_of_games": 3,
                    "opponents": [
                      {
                        "opponent": {
                          "acronym": "WLG",
                          "dark_mode_image_url": null,
                          "id": 126215,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/126215/we_love_gaminglogo_square.png",
                          "location": "GR",
                          "modified_at": "2026-03-10T00:07:30Z",
                          "name": "WLGaming Esports",
                          "slug": "wlgaming-esports-league-of-legends"
                        },
                        "type": "Team"
                      },
                      {
                        "opponent": {
                          "acronym": "USE",
                          "dark_mode_image_url": null,
                          "id": 126832,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/126832/220px_unicorns_of_lovelogo_square.png",
                          "location": "DE",
                          "modified_at": "2026-03-16T12:53:49Z",
                          "name": "Unicorns Of Love Sexy Edition",
                          "slug": "unicorns-of-love-sexy-edition"
                        },
                        "type": "Team"
                      }
                    ],
                    "original_scheduled_at": "2026-03-14T16:00:00Z",
                    "rescheduled": false,
                    "results": [
                      {
                        "score": 1,
                        "team_id": 126215
                      },
                      {
                        "score": 2,
                        "team_id": 126832
                      }
                    ],
                    "scheduled_at": "2026-03-14T16:00:00Z",
                    "serie": {
                      "begin_at": "2026-03-09T16:00:00Z",
                      "end_at": "2026-04-21T22:00:00Z",
                      "full_name": "Winter 2026",
                      "id": 10306,
                      "league_id": 4996,
                      "modified_at": "2026-03-13T22:38:21Z",
                      "name": "",
                      "season": "Winter",
                      "slug": "league-of-legends-emea-masters-winter-2026",
                      "winner_id": null,
                      "winner_type": "Team",
                      "year": 2026
                    },
                    "serie_id": 10306,
                    "slug": "wlgaming-esports-vs-unicorns-of-love-sexy-edition-2026-03-14-b861b451-e692-42a5-a614-97c211f556fb",
                    "status": "finished",
                    "streams_list": [
                      {
                        "embed_url": "https://player.twitch.tv/?channel=obsess3",
                        "language": "de",
                        "main": true,
                        "official": true,
                        "raw_url": "https://www.twitch.tv/obsess3"
                      }
                    ],
                    "tournament": {
                      "begin_at": "2026-03-10T16:00:00Z",
                      "country": null,
                      "detailed_stats": true,
                      "end_at": "2026-03-15T17:44:00Z",
                      "has_bracket": true,
                      "id": 20380,
                      "league_id": 4996,
                      "live_supported": false,
                      "modified_at": "2026-03-16T10:14:11Z",
                      "name": "Group G",
                      "prizepool": null,
                      "region": "WEU",
                      "serie_id": 10306,
                      "slug": "league-of-legends-emea-masters-winter-2026-group-7",
                      "tier": "c",
                      "type": "online",
                      "winner_id": 126832,
                      "winner_type": "Team"
                    },
                    "tournament_id": 20380,
                    "videogame": {
                      "id": 1,
                      "name": "LoL",
                      "slug": "league-of-legends"
                    },
                    "videogame_title": null,
                    "videogame_version": {
                      "current": true,
                      "name": "16.5.1"
                    },
                    "winner": {
                      "acronym": "USE",
                      "dark_mode_image_url": null,
                      "id": 126832,
                      "image_url": "https://cdn-api.pandascore.co/images/team/image/126832/220px_unicorns_of_lovelogo_square.png",
                      "location": "DE",
                      "modified_at": "2026-03-16T12:53:49Z",
                      "name": "Unicorns Of Love Sexy Edition",
                      "slug": "unicorns-of-love-sexy-edition"
                    },
                    "winner_id": 126832,
                    "winner_type": "Team"
                  }
                ]
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLMatches"
            }
          }
        },
        "description": "A list of League-of-Legends matches"
      }
    },
    "schemas": {
      "LoLMatches": {
        "items": {
          "additionalProperties": false,
          "deprecated": false,
          "properties": {
            "begin_at": {
              "deprecated": false,
              "format": "date-time",
              "minLength": 1,
              "nullable": true,
              "title": "MatchBeginAt",
              "type": "string"
            },
            "detailed_stats": {
              "description": "Whether the match offers full stats",
              "title": "MatchDetailedStats",
              "type": "boolean"
            },
            "draw": {
              "description": "Whether result of the match is a draw",
              "title": "MatchIsDraw",
              "type": "boolean"
            },
            "end_at": {
              "deprecated": false,
              "format": "date-time",
              "minLength": 1,
              "nullable": true,
              "title": "MatchEndAt",
              "type": "string"
            },
            "forfeit": {
              "description": "Whether match was forfeited",
              "title": "MatchIsForfeit",
              "type": "boolean"
            },
            "game_advantage": {
              "deprecated": false,
              "description": "ID of the opponent with a game advantage",
              "minimum": 1,
              "nullable": true,
              "title": "GameAdvantageOpponent",
              "type": "integer"
            },
            "games": {
              "items": {
                "additionalProperties": false,
                "deprecated": false,
                "properties": {
                  "begin_at": {
                    "deprecated": false,
                    "description": "The game begin time, UTC.\n`null` when the game status is `not_started`",
                    "format": "date-time",
                    "minLength": 1,
                    "nullable": true,
                    "title": "GameBeginAt",
                    "type": "string"
                  },
                  "complete": {
                    "description": "Whether When `true`, the game statistics are complete and will not be updated again",
                    "title": "GameComplete",
                    "type": "boolean"
                  },
                  "detailed_stats": {
                    "description": "Whether historical data is available for the game",
                    "title": "GameDetailedStats",
                    "type": "boolean"
                  },
                  "end_at": {
                    "deprecated": false,
                    "description": "The game end time, UTC.\n`null` when the game status is not `finished`",
                    "format": "date-time",
                    "minLength": 1,
                    "nullable": true,
                    "title": "GameEndAt",
                    "type": "string"
                  },
                  "finished": {
                    "description": "Whether the game is finished",
                    "title": "GameIsFinished",
                    "type": "boolean"
                  },
                  "forfeit": {
                    "description": "Whether the game has been forfeited",
                    "title": "GameIsForfeit",
                    "type": "boolean"
                  },
                  "id": {
                    "anyOf": [
                      {
                        "description": "LoL game ID",
                        "minimum": 1,
                        "title": "LoLGameID",
                        "type": "integer"
                      },
                      {
                        "description": "Counter-Strike game ID",
                        "minimum": 1,
                        "title": "CSGOGameID",
                        "type": "integer"
                      },
                      {
                        "minimum": 1,
                        "title": "OwGameID",
                        "type": "integer"
                      },
                      {
                        "minimum": 1,
                        "title": "Dota2GameID",
                        "type": "integer"
                      },
                      {
                        "minimum": 1,
                        "title": "PUBGGameID",
                        "type": "integer"
                      },
                      {
                        "minimum": 1,
                        "title": "ValorantGameID",
                        "type": "integer"
                      }
                    ],
                    "description": "ID of the game.\nIDs are video game-specific, ie. a Valorant game and an Overwatch game can have the same game ID.",
                    "title": "GameID"
                  },
                  "length": {
                    "deprecated": false,
                    "description": "Duration of the game in seconds.\n`null` when the game status is not `finished`",
                    "minimum": 0,
                    "nullable": true,
                    "title": "GameLength",
                    "type": "integer"
                  },
                  "match_id": {
                    "minimum": 1,
                    "title": "MatchID",
                    "type": "integer"
                  },
                  "position": {
                    "description": "Game position in the match. Starts at 1",
                    "minimum": 1,
                    "title": "GamePosition",
                    "type": "integer"
                  },
                  "status": {
                    "description": "The game status",
                    "enum": [
                      "finished",
                      "not_played",
                      "not_started",
                      "running"
                    ],
                    "title": "GameStatus",
                    "type": "string"
                  },
                  "winner": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "id": {
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
                      "type": {
                        "deprecated": false,
                        "enum": [
                          "Player",
                          "Team"
                        ],
                        "nullable": true,
                        "title": "OpponentType",
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "type"
                    ],
                    "title": "GameWinner",
                    "type": "object"
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
                  }
                },
                "required": [
                  "begin_at",
                  "complete",
                  "detailed_stats",
                  "end_at",
                  "finished",
                  "forfeit",
                  "id",
                  "length",
                  "match_id",
                  "position",
                  "status",
                  "winner",
                  "winner_type"
                ],
                "title": "Game",
                "type": "object"
              },
              "title": "Games",
              "type": "array"
            },
            "id": {
              "minimum": 1,
              "title": "MatchID",
              "type": "integer"
            },
            "league": {
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
                }
              },
              "required": [
                "id",
                "image_url",
                "modified_at",
                "name",
                "slug",
                "url"
              ],
              "title": "BaseLeague",
              "type": "object"
            },
            "league_id": {
              "minimum": 1,
              "title": "LeagueID",
              "type": "integer"
            },
            "live": {
              "additionalProperties": false,
              "deprecated": false,
              "properties": {
                "opens_at": {
                  "deprecated": false,
                  "format": "date-time",
                  "minLength": 1,
                  "nullable": true,
                  "title": "MatchLiveOpensAt",
                  "type": "string"
                },
                "supported": {
                  "description": "Whether live is supported",
                  "title": "MatchLiveIsSupported",
                  "type": "boolean"
                },
                "url": {
                  "deprecated": false,
                  "format": "uri",
                  "nullable": true,
                  "title": "MatchLiveURL",
                  "type": "string"
                }
              },
              "required": [
                "opens_at",
                "supported",
                "url"
              ],
              "title": "MatchLive",
              "type": "object"
            },
            "low_latency_feed": {
              "additionalProperties": false,
              "deprecated": false,
              "properties": {
                "opens_at": {
                  "deprecated": false,
                  "format": "date-time",
                  "minLength": 1,
                  "nullable": true,
                  "title": "MatchLowLatencyFeedOpensAt",
                  "type": "string"
                },
                "supported": {
                  "description": "Whether low latency feed is supported",
                  "title": "MatchLowLatencyFeedIsSupported",
                  "type": "boolean"
                },
                "url": {
                  "deprecated": false,
                  "format": "uri",
                  "nullable": true,
                  "title": "MatchLowLatencyFeedURL",
                  "type": "string"
                }
              },
              "required": [
                "opens_at",
                "supported",
                "url"
              ],
              "title": "MatchLowLatencyFeed",
              "type": "object"
            },
            "map_picks": {
              "deprecated": false,
              "description": "**Only applies to Valorant matches. The field will not be present on other video games matches.**\nMap picks, `null` when map picks data is unavailable.\n**Important:** `map_picks` field is only present in the response for subscribers of Valorant Historical plan.",
              "items": {
                "additionalProperties": false,
                "deprecated": false,
                "properties": {
                  "id": {
                    "description": "ID of the map",
                    "minimum": 1,
                    "title": "ValorantMapID",
                    "type": "integer"
                  },
                  "image_url": {
                    "description": "URL to an image of the map",
                    "format": "uri",
                    "title": "ValorantMapImageURL",
                    "type": "string"
                  },
                  "name": {
                    "description": "Name of the map",
                    "title": "ValorantMapName",
                    "type": "string"
                  },
                  "picking_team_id": {
                    "deprecated": false,
                    "description": "ID of the team that picked the map",
                    "minimum": 1,
                    "nullable": true,
                    "title": "ValorantPickingTeamID",
                    "type": "integer"
                  },
                  "slug": {
                    "description": "Human-readable identifier of the map",
                    "minLength": 1,
                    "pattern": "^[a-z0-9_-]+$",
                    "title": "ValorantMapSlug",
                    "type": "string"
                  },
                  "videogame_versions": {
                    "description": "Array of of video game versions (ie. patches) for this resource",
                    "items": {
                      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                      "title": "VideogameVersion",
                      "type": "string"
                    },
                    "title": "VideogameVersions",
                    "type": "array"
                  }
                },
                "required": [
                  "id",
                  "image_url",
                  "name",
                  "picking_team_id",
                  "slug",
                  "videogame_versions"
                ],
                "title": "ValorantMapPick",
                "type": "object"
              },
              "nullable": true,
              "title": "ValorantMapPicks",
              "type": "array"
            },
            "match_type": {
              "enum": [
                "all_games_played",
                "best_of",
                "custom",
                "first_to",
                "ow_best_of",
                "red_bull_home_ground"
              ],
              "title": "MatchType",
              "type": "string"
            },
            "modified_at": {
              "format": "date-time",
              "minLength": 1,
              "title": "MatchModifiedAt",
              "type": "string"
            },
            "name": {
              "title": "MatchName",
              "type": "string"
            },
            "number_of_games": {
              "description": "Number of games",
              "minimum": 0,
              "title": "GameCount",
              "type": "integer"
            },
            "opponents": {
              "items": {
                "additionalProperties": false,
                "deprecated": false,
                "properties": {
                  "opponent": {
                    "oneOf": [
                      {
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
                          "age",
                          "birthday",
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
                        "title": "BasePlayer",
                        "type": "object"
                      },
                      {
                        "additionalProperties": false,
                        "deprecated": false,
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
                      }
                    ],
                    "title": "BaseOpponent"
                  },
                  "type": {
                    "enum": [
                      "Player",
                      "Team"
                    ],
                    "title": "OpponentType",
                    "type": "string"
                  }
                },
                "required": [
                  "opponent",
                  "type"
                ],
                "title": "Opponent",
                "type": "object"
              },
              "title": "Opponents",
              "type": "array"
            },
            "original_scheduled_at": {
              "deprecated": false,
              "format": "date-time",
              "minLength": 1,
              "nullable": true,
              "title": "MatchOriginalScheduledAt",
              "type": "string"
            },
            "rescheduled": {
              "deprecated": false,
              "description": "Whether match has been rescheduled",
              "nullable": true,
              "title": "MatchIsRescheduled",
              "type": "boolean"
            },
            "results": {
              "items": {
                "anyOf": [
                  {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "score": {
                        "minimum": 0,
                        "title": "MatchScore",
                        "type": "integer"
                      },
                      "team_id": {
                        "description": "The ID of the team.",
                        "minimum": 1,
                        "title": "TeamID",
                        "type": "integer"
                      }
                    },
                    "required": [
                      "score",
                      "team_id"
                    ],
                    "title": "MatchTeamResult",
                    "type": "object"
                  },
                  {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "player_id": {
                        "description": "ID of the player",
                        "minimum": 1,
                        "title": "PlayerID",
                        "type": "integer"
                      },
                      "score": {
                        "minimum": 0,
                        "title": "MatchScore",
                        "type": "integer"
                      }
                    },
                    "required": [
                      "player_id",
                      "score"
                    ],
                    "title": "MatchPlayerResult",
                    "type": "object"
                  }
                ],
                "title": "MatchResult"
              },
              "title": "MatchResults",
              "type": "array"
            },
            "scheduled_at": {
              "deprecated": false,
              "format": "date-time",
              "minLength": 1,
              "nullable": true,
              "title": "MatchScheduledAt",
              "type": "string"
            },
            "serie": {
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
            "serie_id": {
              "minimum": 1,
              "title": "SerieID",
              "type": "integer"
            },
            "slug": {
              "deprecated": false,
              "minLength": 1,
              "nullable": true,
              "pattern": "^[ a-zA-Z0-9_-]+$",
              "title": "MatchSlug",
              "type": "string"
            },
            "status": {
              "enum": [
                "canceled",
                "finished",
                "not_started",
                "postponed",
                "running"
              ],
              "title": "MatchStatus",
              "type": "string"
            },
            "streams_list": {
              "items": {
                "additionalProperties": false,
                "deprecated": false,
                "properties": {
                  "embed_url": {
                    "deprecated": false,
                    "description": "URL to embed in an iframe.",
                    "format": "uri",
                    "nullable": true,
                    "title": "StreamEmbedURL",
                    "type": "string"
                  },
                  "language": {
                    "description": "Language alpha-2 code according to ISO 649-1 standard.",
                    "enum": [
                      "aa",
                      "ab",
                      "ae",
                      "af",
                      "ak",
                      "am",
                      "an",
                      "ar",
                      "as",
                      "av",
                      "ay",
                      "az",
                      "ba",
                      "be",
                      "bg",
                      "bh",
                      "bi",
                      "bm",
                      "bn",
                      "bo",
                      "br",
                      "bs",
                      "ca",
                      "ce",
                      "ch",
                      "co",
                      "cr",
                      "cs",
                      "cu",
                      "cv",
                      "cy",
                      "da",
                      "de",
                      "dv",
                      "dz",
                      "ee",
                      "el",
                      "en",
                      "eo",
                      "es",
                      "et",
                      "eu",
                      "fa",
                      "ff",
                      "fi",
                      "fj",
                      "fo",
                      "fr",
                      "fy",
                      "ga",
                      "gd",
                      "gl",
                      "gn",
                      "gu",
                      "gv",
                      "ha",
                      "he",
                      "hi",
                      "ho",
                      "hr",
                      "ht",
                      "hu",
                      "hy",
                      "hz",
                      "ia",
                      "id",
                      "ie",
                      "ig",
                      "ii",
                      "ik",
                      "io",
                      "is",
                      "it",
                      "iu",
                      "ja",
                      "jv",
                      "ka",
                      "kg",
                      "ki",
                      "kj",
                      "kk",
                      "kl",
                      "km",
                      "kn",
                      "ko",
                      "kr",
                      "ks",
                      "ku",
                      "kv",
                      "kw",
                      "ky",
                      "la",
                      "lb",
                      "lg",
                      "li",
                      "ln",
                      "lo",
                      "lt",
                      "lu",
                      "lv",
                      "mg",
                      "mh",
                      "mi",
                      "mk",
                      "ml",
                      "mn",
                      "mr",
                      "ms",
                      "mt",
                      "my",
                      "na",
                      "nb",
                      "nd",
                      "ne",
                      "ng",
                      "nl",
                      "nn",
                      "no",
                      "nr",
                      "nv",
                      "ny",
                      "oc",
                      "oj",
                      "om",
                      "or",
                      "os",
                      "pa",
                      "pi",
                      "pl",
                      "ps",
                      "pt",
                      "qu",
                      "rm",
                      "rn",
                      "ro",
                      "ru",
                      "rw",
                      "sa",
                      "sc",
                      "sd",
                      "se",
                      "sg",
                      "si",
                      "sk",
                      "sl",
                      "sm",
                      "sn",
                      "so",
                      "sq",
                      "sr",
                      "ss",
                      "st",
                      "su",
                      "sv",
                      "sw",
                      "ta",
                      "te",
                      "tg",
                      "th",
                      "ti",
                      "tk",
                      "tl",
                      "tn",
                      "to",
                      "tr",
                      "ts",
                      "tt",
                      "tw",
                      "ty",
                      "ug",
                      "uk",
                      "ur",
                      "uz",
                      "ve",
                      "vi",
                      "vo",
                      "wa",
                      "wo",
                      "xh",
                      "yi",
                      "yo",
                      "za",
                      "zh",
                      "zu"
                    ],
                    "title": "StreamLanguage",
                    "type": "string"
                  },
                  "main": {
                    "description": "Whether it is the main stream. Main stream is always official.",
                    "title": "StreamIsMain",
                    "type": "boolean"
                  },
                  "official": {
                    "description": "Whether it is an official broadcast.",
                    "title": "StreamIsOfficial",
                    "type": "boolean"
                  },
                  "raw_url": {
                    "description": "URL to the stream on host website.",
                    "format": "uri",
                    "title": "StreamURL",
                    "type": "string"
                  }
                },
                "required": [
                  "embed_url",
                  "language",
                  "main",
                  "official",
                  "raw_url"
                ],
                "title": "Stream",
                "type": "object"
              },
              "title": "StreamsList",
              "type": "array"
            },
            "tournament": {
              "additionalProperties": false,
              "deprecated": false,
              "properties": {
                "begin_at": {
                  "deprecated": false,
                  "format": "date-time",
                  "minLength": 1,
                  "nullable": true,
                  "title": "TournamentBeginAt",
                  "type": "string"
                },
                "country": {
                  "deprecated": false,
                  "description": "Country code matching the location of the tournament according to the ISO 3166-1 standard (Alpha-2 code). In addition to the standard, the XK code is used for Kosovo. null if unknown",
                  "nullable": true,
                  "title": "TournamentCountry",
                  "type": "string"
                },
                "detailed_stats": {
                  "description": "Whether the tournament is expected to have detailed statistics available",
                  "title": "TournamentDetailedStats",
                  "type": "boolean"
                },
                "end_at": {
                  "deprecated": false,
                  "format": "date-time",
                  "minLength": 1,
                  "nullable": true,
                  "title": "TournamentEndAt",
                  "type": "string"
                },
                "has_bracket": {
                  "description": "Whether the tournament has a bracket",
                  "title": "TournamentHasBracket",
                  "type": "boolean"
                },
                "id": {
                  "minimum": 1,
                  "title": "TournamentID",
                  "type": "integer"
                },
                "league_id": {
                  "minimum": 1,
                  "title": "LeagueID",
                  "type": "integer"
                },
                "live_supported": {
                  "description": "Whether live is supported",
                  "title": "TournamentLiveSupported",
                  "type": "boolean"
                },
                "modified_at": {
                  "format": "date-time",
                  "minLength": 1,
                  "title": "TournamentModifiedAt",
                  "type": "string"
                },
                "name": {
                  "title": "TournamentName",
                  "type": "string"
                },
                "prizepool": {
                  "deprecated": false,
                  "nullable": true,
                  "title": "TournamentPrizepool",
                  "type": "string"
                },
                "region": {
                  "deprecated": false,
                  "description": "Region acronym for the location of the tournament.",
                  "enum": [
                    "AF",
                    "ASIA",
                    "EEU",
                    "ME",
                    "NA",
                    "OCE",
                    "SA",
                    "WEU"
                  ],
                  "nullable": true,
                  "title": "TournamentRegion",
                  "type": "string"
                },
                "serie_id": {
                  "minimum": 1,
                  "title": "SerieID",
                  "type": "integer"
                },
                "slug": {
                  "minLength": 1,
                  "pattern": "^[a-z0-9_-]+$",
                  "title": "TournamentSlug",
                  "type": "string"
                },
                "tier": {
                  "deprecated": false,
                  "description": "The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked'",
                  "enum": [
                    "a",
                    "b",
                    "c",
                    "d",
                    "s",
                    "unranked"
                  ],
                  "nullable": true,
                  "title": "TournamentTier",
                  "type": "string"
                },
                "type": {
                  "deprecated": false,
                  "description": "Location type for a tournament",
                  "enum": [
                    "offline",
                    "online",
                    "online/offline"
                  ],
                  "nullable": true,
                  "title": "TournamentLocationType",
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
                }
              },
              "required": [
                "begin_at",
                "country",
                "detailed_stats",
                "end_at",
                "has_bracket",
                "id",
                "league_id",
                "live_supported",
                "modified_at",
                "name",
                "prizepool",
                "region",
                "serie_id",
                "slug",
                "tier",
                "type",
                "winner_id",
                "winner_type"
              ],
              "title": "BaseTournament",
              "type": "object"
            },
            "tournament_id": {
              "minimum": 1,
              "title": "TournamentID",
              "type": "integer"
            },
            "videogame": {
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
              "title": "CurrentVideogame",
              "type": "object"
            },
            "videogame_title": {
              "additionalProperties": false,
              "deprecated": false,
              "nullable": true,
              "properties": {
                "id": {
                  "minimum": 1,
                  "title": "VideogameTitleID",
                  "type": "integer"
                },
                "name": {
                  "title": "VideogameTitleName",
                  "type": "string"
                },
                "slug": {
                  "minLength": 1,
                  "pattern": "^[a-z0-9_-]+$",
                  "title": "VideogameTitleSlug",
                  "type": "string"
                },
                "videogame_id": {
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
                }
              },
              "required": [
                "id",
                "name",
                "slug",
                "videogame_id"
              ],
              "title": "VideogameTitle",
              "type": "object"
            },
            "videogame_version": {
              "additionalProperties": false,
              "deprecated": false,
              "nullable": true,
              "properties": {
                "current": {
                  "description": "Whether this videogame version is current",
                  "title": "VideogameVersionIsCurrent",
                  "type": "boolean"
                },
                "name": {
                  "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                  "title": "VideogameVersion",
                  "type": "string"
                }
              },
              "required": [
                "current",
                "name"
              ],
              "title": "ShortVideogameVersion",
              "type": "object"
            },
            "winner": {
              "deprecated": false,
              "nullable": true,
              "oneOf": [
                {
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
                    "age",
                    "birthday",
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
                  "title": "BasePlayer",
                  "type": "object"
                },
                {
                  "additionalProperties": false,
                  "deprecated": false,
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
                }
              ],
              "title": "BaseOpponent"
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
              "enum": [
                "Player",
                "Team"
              ],
              "title": "MatchWinnerType",
              "type": "string"
            }
          },
          "required": [
            "begin_at",
            "detailed_stats",
            "draw",
            "end_at",
            "forfeit",
            "game_advantage",
            "games",
            "id",
            "league",
            "league_id",
            "live",
            "match_type",
            "modified_at",
            "name",
            "number_of_games",
            "opponents",
            "original_scheduled_at",
            "rescheduled",
            "results",
            "scheduled_at",
            "serie",
            "serie_id",
            "slug",
            "status",
            "streams_list",
            "tournament",
            "tournament_id",
            "videogame",
            "videogame_title",
            "videogame_version",
            "winner",
            "winner_id",
            "winner_type"
          ],
          "title": "Match",
          "type": "object"
        },
        "title": "LoLMatches",
        "type": "array"
      },
      "filter_over_LoLMatches": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "begin_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "MatchBeginAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "detailed_stats": {
            "description": "Whether the match offers full stats",
            "title": "MatchDetailedStats",
            "type": "boolean"
          },
          "draw": {
            "description": "Whether result of the match is a draw",
            "title": "MatchIsDraw",
            "type": "boolean"
          },
          "end_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "MatchEndAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "finished": {
            "type": "boolean"
          },
          "forfeit": {
            "description": "Whether match was forfeited",
            "title": "MatchIsForfeit",
            "type": "boolean"
          },
          "future": {
            "description": "`true` for future matches only, `false` for past matches only.\nFiltering is done on the `begin_at` value, so  matches with `running` status will not appear if `true`.",
            "type": "boolean"
          },
          "id": {
            "items": {
              "minimum": 1,
              "title": "MatchID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "league_id": {
            "items": {
              "minimum": 1,
              "title": "LeagueID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "match_type": {
            "items": {
              "enum": [
                "all_games_played",
                "best_of",
                "custom",
                "first_to",
                "ow_best_of",
                "red_bull_home_ground"
              ],
              "title": "MatchType",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "modified_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "MatchModifiedAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "MatchName",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "not_started": {
            "type": "boolean"
          },
          "number_of_games": {
            "items": {
              "description": "Number of games",
              "minimum": 0,
              "title": "GameCount",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "opponent_id": {
            "description": "A Team or a Player (id or slug). You can use`filter[winner_type]=Team` or `filter[winner_type]=Player` to focus on teams or players.",
            "items": {
              "oneOf": [
                {
                  "description": "A team ID or slug",
                  "oneOf": [
                    {
                      "description": "The ID of the team.",
                      "minimum": 1,
                      "title": "TeamID",
                      "type": "integer"
                    },
                    {
                      "minLength": 1,
                      "pattern": "^[a-z0-9_-]+$",
                      "title": "TeamSlug",
                      "type": "string"
                    }
                  ],
                  "title": "TeamIDOrSlug"
                },
                {
                  "description": "A player ID or slug",
                  "oneOf": [
                    {
                      "description": "ID of the player",
                      "minimum": 1,
                      "title": "PlayerID",
                      "type": "integer"
                    },
                    {
                      "description": "Unique, human-readable identifier for the player.\n`id` and `slug` can be used interchangeably throughout the API.",
                      "minLength": 1,
                      "pattern": "^[a-z0-9_-]+$",
                      "title": "PlayerSlug",
                      "type": "string"
                    }
                  ],
                  "title": "PlayerIDOrSlug"
                }
              ]
            },
            "minItems": 1,
            "type": "array"
          },
          "opponents_filled": {
            "description": "Whether a match has opponents filled i.e. opponents are not TBD.",
            "type": "boolean"
          },
          "past": {
            "type": "boolean"
          },
          "running": {
            "type": "boolean"
          },
          "scheduled_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "MatchScheduledAt",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "serie_id": {
            "items": {
              "minimum": 1,
              "title": "SerieID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "slug": {
            "items": {
              "minLength": 1,
              "pattern": "^[ a-zA-Z0-9_-]+$",
              "title": "MatchSlug",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "status": {
            "items": {
              "enum": [
                "canceled",
                "finished",
                "not_started",
                "postponed",
                "running"
              ],
              "title": "MatchStatus",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          },
          "tournament_id": {
            "items": {
              "minimum": 1,
              "title": "TournamentID",
              "type": "integer"
            },
            "minItems": 1,
            "type": "array"
          },
          "unscheduled": {
            "type": "boolean"
          },
          "videogame": {
            "items": {
              "description": "A videogame ID or slug",
              "oneOf": [
                {
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
                {
                  "description": "A videogame slug",
                  "enum": [
                    "cod-mw",
                    "cs-go",
                    "dota-2",
                    "e-basketball",
                    "e-cricket",
                    "e-hockey",
                    "e-soccer",
                    "e-tennis",
                    "fifa",
                    "kog",
                    "league-of-legends",
                    "lol-wild-rift",
                    "mlbb",
                    "ow",
                    "pubg",
                    "r6-siege",
                    "rl",
                    "starcraft-2",
                    "starcraft-brood-war",
                    "valorant"
                  ],
                  "title": "VideogameSlug",
                  "type": "string"
                }
              ],
              "title": "VideogameIDOrSlug"
            },
            "minItems": 1,
            "type": "array"
          },
          "videogame_title": {
            "description": "A videogame title id or slug.\nOnly for `/csgo/*`, `/codmw/*`, `/fifa/*` and `/ow/*` endpoints\n",
            "items": {
              "oneOf": [
                {
                  "minimum": 1,
                  "title": "VideogameTitleID",
                  "type": "integer"
                },
                {
                  "minLength": 1,
                  "pattern": "^[a-z0-9_-]+$",
                  "title": "VideogameTitleSlug",
                  "type": "string"
                }
              ]
            },
            "minItems": 1,
            "type": "array"
          },
          "videogame_version": {
            "description": "Filter by the names of videogame versions, all versions using `filter[videogame_version]=all`, or by the latest version using `filter[videogame_version]=latest`\nOnly for `valorant/*` and `/lol/*` endpoints.\n",
            "items": {
              "oneOf": [
                {
                  "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$",
                  "title": "VideogameVersion",
                  "type": "string"
                },
                {
                  "enum": [
                    "all"
                  ]
                },
                {
                  "enum": [
                    "latest"
                  ]
                }
              ]
            },
            "minItems": 1,
            "type": "array"
          },
          "winner_id": {
            "items": {
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
              "title": "OpponentID"
            },
            "minItems": 1,
            "type": "array"
          },
          "winner_type": {
            "items": {
              "enum": [
                "Player",
                "Team"
              ],
              "title": "MatchWinnerType",
              "type": "string"
            },
            "minItems": 1,
            "type": "array"
          }
        },
        "type": "object"
      },
      "range_over_LoLMatches": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "begin_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "MatchBeginAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "detailed_stats": {
            "items": {
              "description": "Whether the match offers full stats",
              "title": "MatchDetailedStats",
              "type": "boolean"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "draw": {
            "items": {
              "description": "Whether result of the match is a draw",
              "title": "MatchIsDraw",
              "type": "boolean"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "end_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "MatchEndAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "forfeit": {
            "items": {
              "description": "Whether match was forfeited",
              "title": "MatchIsForfeit",
              "type": "boolean"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "id": {
            "items": {
              "minimum": 1,
              "title": "MatchID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "match_type": {
            "items": {
              "enum": [
                "all_games_played",
                "best_of",
                "custom",
                "first_to",
                "ow_best_of",
                "red_bull_home_ground"
              ],
              "title": "MatchType",
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
              "title": "MatchModifiedAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "name": {
            "items": {
              "title": "MatchName",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "number_of_games": {
            "items": {
              "description": "Number of games",
              "minimum": 0,
              "title": "GameCount",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "scheduled_at": {
            "items": {
              "format": "date-time",
              "minLength": 1,
              "title": "MatchScheduledAt",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "slug": {
            "items": {
              "minLength": 1,
              "pattern": "^[ a-zA-Z0-9_-]+$",
              "title": "MatchSlug",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "status": {
            "items": {
              "enum": [
                "canceled",
                "finished",
                "not_started",
                "postponed",
                "running"
              ],
              "title": "MatchStatus",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "tournament_id": {
            "items": {
              "minimum": 1,
              "title": "TournamentID",
              "type": "integer"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "winner_id": {
            "items": {
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
              "title": "OpponentID"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          },
          "winner_type": {
            "items": {
              "enum": [
                "Player",
                "Team"
              ],
              "title": "MatchWinnerType",
              "type": "string"
            },
            "maxItems": 2,
            "minItems": 2,
            "type": "array"
          }
        },
        "type": "object"
      },
      "search_over_LoLMatches": {
        "additionalProperties": false,
        "minProperties": 1,
        "properties": {
          "match_type": {
            "enum": [
              "all_games_played",
              "best_of",
              "custom",
              "first_to",
              "ow_best_of",
              "red_bull_home_ground"
            ],
            "title": "MatchType",
            "type": "string"
          },
          "name": {
            "title": "MatchName",
            "type": "string"
          },
          "slug": {
            "minLength": 1,
            "pattern": "^[ a-zA-Z0-9_-]+$",
            "title": "MatchSlug",
            "type": "string"
          },
          "status": {
            "enum": [
              "canceled",
              "finished",
              "not_started",
              "postponed",
              "running"
            ],
            "title": "MatchStatus",
            "type": "string"
          },
          "winner_type": {
            "enum": [
              "Player",
              "Team"
            ],
            "title": "MatchWinnerType",
            "type": "string"
          }
        },
        "type": "object"
      },
      "sort_over_LoLMatches": {
        "items": {
          "enum": [
            "begin_at",
            "-begin_at",
            "detailed_stats",
            "-detailed_stats",
            "draw",
            "-draw",
            "end_at",
            "-end_at",
            "forfeit",
            "-forfeit",
            "id",
            "-id",
            "match_type",
            "-match_type",
            "modified_at",
            "-modified_at",
            "name",
            "-name",
            "number_of_games",
            "-number_of_games",
            "scheduled_at",
            "-scheduled_at",
            "slug",
            "-slug",
            "status",
            "-status",
            "tournament_id",
            "-tournament_id",
            "winner_id",
            "-winner_id",
            "winner_type",
            "-winner_type"
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
    "/lol/matches": {
      "get": {
        "description": "List matches for the League of Legends videogame\n> ℹ️  \n> \n> This endpoint is available to all customers",
        "operationId": "get_lol_matches",
        "parameters": [
          {
            "description": "Options to filter results. String fields are case sensitive\nFor more information on filtering, see [docs](/docs/filtering-and-sorting#filter).",
            "explode": true,
            "in": "query",
            "name": "filter",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/filter_over_LoLMatches"
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
              "$ref": "#/components/schemas/range_over_LoLMatches"
            },
            "style": "deepObject"
          },
          {
            "description": "Options to sort results\nFor more information on sorting, see [docs](/docs/filtering-and-sorting#sort).",
            "in": "query",
            "name": "sort",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/sort_over_LoLMatches"
            }
          },
          {
            "description": "Options to search results\nFor more information on searching, see [docs](/docs/filtering-and-sorting#search).",
            "explode": true,
            "in": "query",
            "name": "search",
            "required": false,
            "schema": {
              "$ref": "#/components/schemas/search_over_LoLMatches"
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
            "$ref": "#/components/responses/LoLMatches"
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
        "summary": "List LoL matches",
        "tags": [
          "LoL matches"
        ],
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/matches' \\\n     --header 'accept: application/json'\n",
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