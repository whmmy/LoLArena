> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a LoL match

Get a single League of Legends match by ID or slug
> ℹ️  
> 
> This endpoint is only available to customers with a historical or real-time data plan

# OpenAPI definition

```json
{
  "components": {
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
      "LoLMatch": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/matches/649708": {
                "description": "/lol/matches/649708",
                "value": {
                  "begin_at": "2022-09-29T20:32:51Z",
                  "detailed_stats": true,
                  "draw": false,
                  "end_at": "2022-09-29T21:22:57Z",
                  "forfeit": false,
                  "game_advantage": null,
                  "games": [
                    {
                      "begin_at": "2022-09-29T20:32:51Z",
                      "complete": true,
                      "detailed_stats": true,
                      "end_at": "2022-09-29T21:22:58Z",
                      "finished": true,
                      "forfeit": false,
                      "id": 239131,
                      "length": 2278,
                      "match_id": 649708,
                      "players": [
                        {
                          "assists": 7,
                          "deaths": 5,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "kills": 0,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 0,
                            "turrets": 0,
                            "wards": 4
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 0,
                          "player_id": 566,
                          "role": "sup"
                        },
                        {
                          "assists": 7,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 6,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 3,
                            "turrets": 1,
                            "wards": 13
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "player_id": 773,
                          "role": "mid"
                        },
                        {
                          "assists": 5,
                          "deaths": 7,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 1,
                            "wards": 11
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "player_id": 1019,
                          "role": "top"
                        },
                        {
                          "assists": 7,
                          "deaths": 6,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "kills": 5,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 171,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 5,
                            "turrets": 3,
                            "wards": 37
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 2,
                          "player_id": 9199,
                          "role": "jun"
                        },
                        {
                          "assists": 5,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 18,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 3,
                            "turrets": 0,
                            "wards": 9
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 911,
                          "largest_killing_spree": 3,
                          "largest_multi_kill": 2,
                          "player_id": 26976,
                          "role": "adc"
                        },
                        {
                          "assists": 8,
                          "deaths": 4,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": true,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": true,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "kills": 8,
                          "kills_counters": {
                            "inhibitors": 1,
                            "neutral_minions": 72,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 8,
                            "turrets": 1,
                            "wards": 6
                          },
                          "kills_series": {
                            "double_kills": 1,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 3,
                          "largest_multi_kill": 2,
                          "player_id": 1284,
                          "role": "mid"
                        },
                        {
                          "assists": 10,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": true,
                            "first_tower_kill": false
                          },
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 34,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 3,
                            "turrets": 3,
                            "wards": 18
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 2,
                          "largest_killing_spree": 2,
                          "largest_multi_kill": 1,
                          "player_id": 3546,
                          "role": "top"
                        },
                        {
                          "assists": 9,
                          "deaths": 3,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "kills": 1,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 0,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 1,
                            "turrets": 0,
                            "wards": 16
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 0,
                          "largest_multi_kill": 1,
                          "player_id": 18037,
                          "role": "sup"
                        },
                        {
                          "assists": 10,
                          "deaths": 2,
                          "flags": {
                            "first_blood_assist": false,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": true,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": true
                          },
                          "kills": 7,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 191,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 7,
                            "turrets": 4,
                            "wards": 25
                          },
                          "kills_series": {
                            "double_kills": 2,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 190,
                          "largest_killing_spree": 3,
                          "largest_multi_kill": 2,
                          "player_id": 24428,
                          "role": "jun"
                        },
                        {
                          "assists": 11,
                          "deaths": 1,
                          "flags": {
                            "first_blood_assist": true,
                            "first_blood_kill": false,
                            "first_inhibitor_assist": false,
                            "first_inhibitor_kill": false,
                            "first_tower_assist": false,
                            "first_tower_kill": false
                          },
                          "kills": 3,
                          "kills_counters": {
                            "inhibitors": 0,
                            "neutral_minions": 22,
                            "neutral_minions_enemy_jungle": null,
                            "neutral_minions_team_jungle": null,
                            "players": 3,
                            "turrets": 1,
                            "wards": 14
                          },
                          "kills_series": {
                            "double_kills": 0,
                            "penta_kills": 0,
                            "quadra_kills": 0,
                            "triple_kills": 0
                          },
                          "largest_critical_strike": 0,
                          "largest_killing_spree": 3,
                          "largest_multi_kill": 1,
                          "player_id": 25825,
                          "role": "adc"
                        }
                      ],
                      "position": 1,
                      "status": "finished",
                      "winner": {
                        "id": 126536,
                        "type": "Team"
                      },
                      "winner_type": "Team"
                    }
                  ],
                  "id": 649708,
                  "league": {
                    "id": 297,
                    "image_url": "https://cdn-api.pandascore.co/images/league/image/297/worlds-png",
                    "modified_at": "2023-12-06T15:53:28Z",
                    "name": "Worlds",
                    "slug": "league-of-legends-world-championship",
                    "url": null
                  },
                  "league_id": 297,
                  "live": {
                    "opens_at": "2022-09-29T20:17:51.000000Z",
                    "supported": true,
                    "url": "wss://live.pandascore.co/matches/649708"
                  },
                  "match_type": "best_of",
                  "modified_at": "2022-10-19T08:37:09Z",
                  "name": "ISG vs MAD",
                  "number_of_games": 1,
                  "opponents": [
                    {
                      "opponent": {
                        "acronym": "ISG",
                        "dark_mode_image_url": null,
                        "id": 147,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/147/isuruslogo_square.png",
                        "location": "AR",
                        "modified_at": "2025-12-04T08:32:14Z",
                        "name": "Isurus",
                        "slug": "isurus-gaming"
                      },
                      "type": "Team"
                    },
                    {
                      "opponent": {
                        "acronym": "MKOI",
                        "dark_mode_image_url": null,
                        "id": 126536,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/126536/movistar_ko_ilogo_square.png",
                        "location": "ES",
                        "modified_at": "2026-02-08T22:16:50Z",
                        "name": "Movistar KOI",
                        "slug": "mad-lions-league-of-legends"
                      },
                      "type": "Team"
                    }
                  ],
                  "original_scheduled_at": "2022-09-30T00:00:00Z",
                  "players": [
                    {
                      "assists": 7,
                      "deaths": 5,
                      "first_name": "Son",
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/566/isg_jelly_2023_opening.png",
                      "kills": 0,
                      "last_name": "Ho-gyeong",
                      "name": "Jelly",
                      "nationality": "KR",
                      "number_of_games": 1,
                      "player_id": 566,
                      "role": "sup",
                      "slug": "jelly"
                    },
                    {
                      "assists": 7,
                      "deaths": 2,
                      "first_name": "Ali",
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/773/220px-ISG_Seiya_2019_Split_2.png",
                      "kills": 3,
                      "last_name": "Bracamontes",
                      "name": "Seiya",
                      "nationality": "MX",
                      "number_of_games": 1,
                      "player_id": 773,
                      "role": "mid",
                      "slug": "seiya"
                    },
                    {
                      "assists": 5,
                      "deaths": 7,
                      "first_name": "Geon-mo",
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/1019/sn_add_2021_split_1.png",
                      "kills": 1,
                      "last_name": "Kang",
                      "name": "ADD",
                      "nationality": "KR",
                      "number_of_games": 1,
                      "player_id": 1019,
                      "role": "top",
                      "slug": "add"
                    },
                    {
                      "assists": 8,
                      "deaths": 4,
                      "first_name": "Yasin",
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/1284/sk_nisqy_2024_split_1.png",
                      "kills": 8,
                      "last_name": "Dinçer",
                      "name": "Nisqy",
                      "nationality": "BE",
                      "number_of_games": 1,
                      "player_id": 1284,
                      "role": "mid",
                      "slug": "nisqy"
                    },
                    {
                      "assists": 10,
                      "deaths": 2,
                      "first_name": "İrfan",
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/3546/ezgif_64c6d21bfd4ce606.png",
                      "kills": 3,
                      "last_name": "Berk Tükek",
                      "name": "Armut",
                      "nationality": "TR",
                      "number_of_games": 1,
                      "player_id": 3546,
                      "role": "top",
                      "slug": "push2win"
                    },
                    {
                      "assists": 7,
                      "deaths": 6,
                      "first_name": "Jesús  Alberto",
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/9199/isg_grell_2023_opening.png",
                      "kills": 5,
                      "last_name": "Loya Trujillo",
                      "name": "Grell",
                      "nationality": "MX",
                      "number_of_games": 1,
                      "player_id": 9199,
                      "role": "jun",
                      "slug": "grell"
                    },
                    {
                      "assists": 9,
                      "deaths": 3,
                      "first_name": "Norman",
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/18037/th_kaiser_2024_split_1.png",
                      "kills": 1,
                      "last_name": "Kaiser",
                      "name": "Kaiser",
                      "nationality": "DE",
                      "number_of_games": 1,
                      "player_id": 18037,
                      "role": "sup",
                      "slug": "gistick"
                    },
                    {
                      "assists": 10,
                      "deaths": 2,
                      "first_name": "Javier",
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/24428/mkoi_elyoya_2025_split_3.png",
                      "kills": 7,
                      "last_name": "Prades",
                      "name": "Elyoya",
                      "nationality": "ES",
                      "number_of_games": 1,
                      "player_id": 24428,
                      "role": "jun",
                      "slug": "elyoya"
                    },
                    {
                      "assists": 11,
                      "deaths": 1,
                      "first_name": "William",
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/25825/eg_unf0_rgiven_2023_split_2.png",
                      "kills": 3,
                      "last_name": "Nieminen",
                      "name": "UNF0RGIVEN",
                      "nationality": "SE",
                      "number_of_games": 1,
                      "player_id": 25825,
                      "role": "adc",
                      "slug": "unforgiven-william-nieminen"
                    },
                    {
                      "assists": 5,
                      "deaths": 2,
                      "first_name": "Omar André",
                      "image_url": "https://cdn-api.pandascore.co/images/player/image/26976/isg_gavotto_2023_opening.png",
                      "kills": 3,
                      "last_name": "Gavotto",
                      "name": "Gavotto",
                      "nationality": "MX",
                      "number_of_games": 1,
                      "player_id": 26976,
                      "role": "adc",
                      "slug": "pix-gavotto"
                    }
                  ],
                  "rescheduled": true,
                  "results": [
                    {
                      "score": 0,
                      "team_id": 147
                    },
                    {
                      "score": 1,
                      "team_id": 126536
                    }
                  ],
                  "scheduled_at": "2022-09-29T20:00:00Z",
                  "serie": {
                    "begin_at": "2022-09-28T22:00:00Z",
                    "end_at": "2022-11-06T05:25:00Z",
                    "full_name": "2022",
                    "id": 5065,
                    "league_id": 297,
                    "modified_at": "2022-11-08T16:14:11Z",
                    "name": null,
                    "season": null,
                    "slug": "league-of-legends-world-championship-2022",
                    "winner_id": 126370,
                    "winner_type": "Team",
                    "year": 2022
                  },
                  "serie_id": 5065,
                  "slug": "2022-09-30-74e65a17-a392-4128-8ed6-fbce350bfbab",
                  "status": "finished",
                  "streams_list": [
                    {
                      "embed_url": null,
                      "language": "en",
                      "main": true,
                      "official": true,
                      "raw_url": "http://www.twitch.tv/riotgames"
                    },
                    {
                      "embed_url": "https://player.twitch.tv/?channel=lck_korea",
                      "language": "ko",
                      "main": false,
                      "official": false,
                      "raw_url": "https://www.twitch.tv/lck_korea"
                    },
                    {
                      "embed_url": "https://player.twitch.tv/?channel=otplol_",
                      "language": "fr",
                      "main": false,
                      "official": false,
                      "raw_url": "https://www.twitch.tv/otplol_"
                    }
                  ],
                  "tournament": {
                    "begin_at": "2022-09-28T22:00:00Z",
                    "country": null,
                    "detailed_stats": true,
                    "end_at": "2022-10-03T01:45:00Z",
                    "has_bracket": false,
                    "id": 8934,
                    "league_id": 297,
                    "live_supported": true,
                    "modified_at": "2022-11-08T16:14:11Z",
                    "name": "Play-In Group B",
                    "prizepool": null,
                    "region": null,
                    "serie_id": 5065,
                    "slug": "league-of-legends-world-championship-2022-play-in-group-b",
                    "tier": "s",
                    "type": null,
                    "winner_id": null,
                    "winner_type": "Team"
                  },
                  "tournament_id": 8934,
                  "videogame_title": null,
                  "videogame_version": {
                    "current": false,
                    "name": "12.18.1"
                  },
                  "winner": {
                    "acronym": "MKOI",
                    "dark_mode_image_url": null,
                    "id": 126536,
                    "image_url": "https://cdn-api.pandascore.co/images/team/image/126536/movistar_ko_ilogo_square.png",
                    "location": "ES",
                    "modified_at": "2026-02-08T22:16:50Z",
                    "name": "Movistar KOI",
                    "slug": "mad-lions-league-of-legends"
                  },
                  "winner_id": 126536,
                  "winner_type": "Team"
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLMatch"
            }
          }
        },
        "description": "A League-of-Legends match"
      }
    },
    "schemas": {
      "LoLMatch": {
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
                  "description": "LoL game ID",
                  "minimum": 1,
                  "title": "LoLGameID",
                  "type": "integer"
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
                "players": {
                  "deprecated": false,
                  "items": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "description": "Player's data for a Game in a LoL Match",
                    "properties": {
                      "assists": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAssistCount",
                        "type": "integer"
                      },
                      "deaths": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLDeathCount",
                        "type": "integer"
                      },
                      "flags": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "first_blood_assist": {
                            "deprecated": false,
                            "description": "Whether player got first blood assist",
                            "nullable": true,
                            "title": "LoLGotFirstBloodAssist",
                            "type": "boolean"
                          },
                          "first_blood_kill": {
                            "deprecated": false,
                            "description": "Whether player got first blood kill",
                            "nullable": true,
                            "title": "LoLGotFirstBloodKill",
                            "type": "boolean"
                          },
                          "first_inhibitor_assist": {
                            "deprecated": false,
                            "description": "Whether player got first inhibitor assist",
                            "nullable": true,
                            "title": "LoLGotFirstInhibitorAssist",
                            "type": "boolean"
                          },
                          "first_inhibitor_kill": {
                            "deprecated": false,
                            "description": "Whether player got first inhibitor kill",
                            "nullable": true,
                            "title": "LoLGotFirstInhibitorKill",
                            "type": "boolean"
                          },
                          "first_tower_assist": {
                            "deprecated": false,
                            "description": "Whether player got first tower assist",
                            "nullable": true,
                            "title": "LoLGotGirstTowerAssist",
                            "type": "boolean"
                          },
                          "first_tower_kill": {
                            "deprecated": false,
                            "description": "Whether player got first tower kill",
                            "nullable": true,
                            "title": "LoLGotFirstTowerKill",
                            "type": "boolean"
                          }
                        },
                        "required": [
                          "first_blood_assist",
                          "first_blood_kill",
                          "first_inhibitor_assist",
                          "first_inhibitor_kill",
                          "first_tower_assist",
                          "first_tower_kill"
                        ],
                        "title": "LoLFlags",
                        "type": "object"
                      },
                      "kills": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLKillCount",
                        "type": "integer"
                      },
                      "kills_counters": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "inhibitors": {
                            "deprecated": false,
                            "description": "Number of inhibitors killed by the player",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLInhibitorCount",
                            "type": "integer"
                          },
                          "neutral_minions": {
                            "deprecated": false,
                            "description": "Creep Score awarded for killing neutral minions.\n\nNB: This can be different than the actual number of neutral minions killed.",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLNeutralMinionCount",
                            "type": "integer"
                          },
                          "neutral_minions_enemy_jungle": {
                            "deprecated": false,
                            "description": "Creep Score awarded for killing neutral minions in the player's enemy jungle.\n\nNB: This can be different than the actual number of neutral minions killed.",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLNeutralMinionsEnemyJungleCount",
                            "type": "integer"
                          },
                          "neutral_minions_team_jungle": {
                            "deprecated": false,
                            "description": "Creep Score awarded for killing neutral minions in the player's team jungle.\n\nNB: This can be different than the actual number of neutral minions killed.",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLNeutralMinionsTeamJungleCount",
                            "type": "integer"
                          },
                          "players": {
                            "deprecated": false,
                            "description": "Number of players killed",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLPlayerCount",
                            "type": "integer"
                          },
                          "turrets": {
                            "deprecated": false,
                            "description": "Number of turrets killed",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLTurretCount",
                            "type": "integer"
                          },
                          "wards": {
                            "deprecated": false,
                            "description": "Number of wards killed by the player",
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLWardCount",
                            "type": "integer"
                          }
                        },
                        "required": [
                          "inhibitors",
                          "neutral_minions",
                          "neutral_minions_enemy_jungle",
                          "neutral_minions_team_jungle",
                          "players",
                          "turrets",
                          "wards"
                        ],
                        "title": "LoLKillCounters",
                        "type": "object"
                      },
                      "kills_series": {
                        "additionalProperties": false,
                        "deprecated": false,
                        "properties": {
                          "double_kills": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLKillsSerieDouble",
                            "type": "integer"
                          },
                          "penta_kills": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLKillsSeriePenta",
                            "type": "integer"
                          },
                          "quadra_kills": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLKillsSerieQuadra",
                            "type": "integer"
                          },
                          "triple_kills": {
                            "deprecated": false,
                            "minimum": 0,
                            "nullable": true,
                            "title": "LoLKillsSerieTriple",
                            "type": "integer"
                          }
                        },
                        "required": [
                          "double_kills",
                          "penta_kills",
                          "quadra_kills",
                          "triple_kills"
                        ],
                        "title": "LoLKillsSeries",
                        "type": "object"
                      },
                      "largest_critical_strike": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLLargestCriticalStrike",
                        "type": "integer"
                      },
                      "largest_killing_spree": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLLargestKillingSpree",
                        "type": "integer"
                      },
                      "largest_multi_kill": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLLargestMultiKill",
                        "type": "integer"
                      },
                      "player_id": {
                        "description": "ID of the player",
                        "minimum": 1,
                        "title": "PlayerID",
                        "type": "integer"
                      },
                      "role": {
                        "deprecated": false,
                        "enum": [
                          "adc",
                          "jun",
                          "mid",
                          "sup",
                          "top"
                        ],
                        "nullable": true,
                        "title": "LoLPlayerRole",
                        "type": "string"
                      }
                    },
                    "required": [
                      "assists",
                      "deaths",
                      "flags",
                      "kills",
                      "kills_counters",
                      "kills_series",
                      "largest_critical_strike",
                      "largest_killing_spree",
                      "largest_multi_kill",
                      "player_id",
                      "role"
                    ],
                    "title": "LoLMatchGamePlayer",
                    "type": "object"
                  },
                  "nullable": true,
                  "title": "LoLMatchGamePlayers",
                  "type": "array"
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
                "players",
                "position",
                "status",
                "winner",
                "winner_type"
              ],
              "title": "LoLMatchGame",
              "type": "object"
            },
            "title": "LoLMatchGames",
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
          "players": {
            "items": {
              "additionalProperties": false,
              "deprecated": false,
              "description": "Player's data for a LoL Match",
              "properties": {
                "assists": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLAssistCount",
                  "type": "integer"
                },
                "deaths": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLDeathCount",
                  "type": "integer"
                },
                "first_name": {
                  "deprecated": false,
                  "description": "First name of the player. `null` if unknown",
                  "nullable": true,
                  "title": "PlayerFirstName",
                  "type": "string"
                },
                "image_url": {
                  "deprecated": false,
                  "description": "URL to the photo of the player. `null` if not available.",
                  "format": "uri",
                  "nullable": true,
                  "title": "PlayerImageURL",
                  "type": "string"
                },
                "kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLKillCount",
                  "type": "integer"
                },
                "last_name": {
                  "deprecated": false,
                  "description": "Last name of the player. `null` if unknown",
                  "nullable": true,
                  "title": "PlayerLastName",
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
                "number_of_games": {
                  "description": "Number of games",
                  "minimum": 0,
                  "title": "GameCount",
                  "type": "integer"
                },
                "player_id": {
                  "description": "ID of the player",
                  "minimum": 1,
                  "title": "PlayerID",
                  "type": "integer"
                },
                "role": {
                  "deprecated": false,
                  "enum": [
                    "adc",
                    "jun",
                    "mid",
                    "sup",
                    "top"
                  ],
                  "nullable": true,
                  "title": "LoLPlayerRole",
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
                "assists",
                "deaths",
                "first_name",
                "image_url",
                "kills",
                "last_name",
                "name",
                "nationality",
                "number_of_games",
                "player_id",
                "role",
                "slug"
              ],
              "title": "LoLMatchPlayer",
              "type": "object"
            },
            "title": "LoLMatchPlayers",
            "type": "array"
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
          "players",
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
          "videogame_title",
          "videogame_version",
          "winner",
          "winner_id",
          "winner_type"
        ],
        "title": "LoLMatch",
        "type": "object"
      },
      "MatchIDOrSlug": {
        "description": "A match ID or slug",
        "oneOf": [
          {
            "minimum": 1,
            "title": "MatchID",
            "type": "integer"
          },
          {
            "minLength": 1,
            "pattern": "^[ a-zA-Z0-9_-]+$",
            "title": "MatchSlug",
            "type": "string"
          }
        ],
        "title": "MatchIDOrSlug"
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
    "/lol/matches/{match_id_or_slug}": {
      "get": {
        "description": "Get a single League of Legends match by ID or slug\n> ℹ️  \n> \n> This endpoint is only available to customers with a historical or real-time data plan",
        "operationId": "get_lol_matches_matchIdOrSlug",
        "parameters": [
          {
            "description": "A match ID or slug",
            "in": "path",
            "name": "match_id_or_slug",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/MatchIDOrSlug"
            }
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLMatch"
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
        "summary": "Get a LoL match",
        "tags": [
          "LoL matches"
        ],
        "x-pandascore-plan": "Historical plan",
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/matches/{match_id_or_slug}' \\\n     --header 'accept: application/json'\n",
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