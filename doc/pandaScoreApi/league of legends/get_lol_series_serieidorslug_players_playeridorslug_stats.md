> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get stats for LoL player on serie

Get detailed statistics of a given League-of-Legends player for the given serie
> ℹ️  
> 
> This endpoint is only available to customers with a historical or real-time data plan

# OpenAPI definition

```json
{
  "components": {
    "parameters": {
      "GamesCount": {
        "description": "The amount of games used for the statistics.\n\nFor example if `?games_count=5`, it would show the statistics for the most recent 5 games played\n",
        "in": "query",
        "name": "games_count",
        "required": false,
        "schema": {
          "type": "integer"
        }
      },
      "LoLStatsSide": {
        "in": "query",
        "name": "side",
        "required": false,
        "schema": {
          "enum": [
            "blue",
            "red"
          ],
          "type": "string"
        }
      },
      "StatsFrom": {
        "description": "Filter out 'from' date",
        "in": "query",
        "name": "from",
        "required": false,
        "schema": {
          "example": "2017-07-21",
          "format": "date",
          "type": "string"
        }
      },
      "StatsTo": {
        "description": "Filter out 'to' date",
        "in": "query",
        "name": "to",
        "required": false,
        "schema": {
          "example": "2017-07-21",
          "format": "date",
          "type": "string"
        }
      },
      "StatsVideogameVersion": {
        "in": "query",
        "name": "videogame_version",
        "required": false,
        "schema": {
          "$ref": "#/components/schemas/VideogameVersionOrAll"
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
      "LoLStatsForPlayerBySerie": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/series/5065/players/585/stats": {
                "description": "/lol/series/5065/players/585/stats",
                "value": {
                  "active": true,
                  "age": 29,
                  "birthday": "1996-05-07",
                  "current_team": {
                    "acronym": "T1",
                    "dark_mode_image_url": null,
                    "id": 126061,
                    "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                    "location": "KR",
                    "modified_at": "2025-09-24T08:31:48Z",
                    "name": "T1",
                    "slug": "t1"
                  },
                  "current_videogame": {
                    "id": 1,
                    "name": "LoL",
                    "slug": "league-of-legends"
                  },
                  "favorite_champions": [
                    {
                      "champion": {
                        "armor": 23,
                        "armorperlevel": 4.7,
                        "attackdamage": 62,
                        "attackdamageperlevel": 3.3,
                        "attackrange": 125,
                        "attackspeedoffset": null,
                        "attackspeedperlevel": 3.2,
                        "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/fef8d395b9ec3d54324441e5abd368a6.jpg",
                        "crit": 0,
                        "critperlevel": 0,
                        "hp": 570,
                        "hpperlevel": 119,
                        "hpregen": 9,
                        "hpregenperlevel": 0.9,
                        "id": 2982,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/254171517c5418e10285bba695dfa951.png",
                        "movespeed": 345,
                        "mp": 200,
                        "mpperlevel": 0,
                        "mpregen": 50,
                        "mpregenperlevel": 0,
                        "name": "Akali",
                        "slug": "Akali",
                        "spellblock": 37,
                        "spellblockperlevel": 2.05,
                        "videogame_versions": [
                          "14.7.1",
                          "14.6.1",
                          "14.5.1",
                          "14.4.1",
                          "14.3.1",
                          "14.2.1",
                          "14.1.1",
                          "13.24.1",
                          "13.23.1",
                          "13.22.1",
                          "13.21.1",
                          "13.20.1",
                          "13.19.1",
                          "13.18.1",
                          "13.17.1",
                          "13.16.1",
                          "13.15.1",
                          "13.14.1",
                          "13.13.1",
                          "13.12.1",
                          "13.11.1",
                          "13.10.1",
                          "13.9.1",
                          "13.8.1",
                          "13.7.1",
                          "13.6.1",
                          "13.5.1",
                          "13.4.1",
                          "13.3.1",
                          "13.1.1",
                          "12.23.1",
                          "12.22.1",
                          "12.21.1",
                          "12.20.1",
                          "12.19.1",
                          "12.18.1",
                          "12.17.1",
                          "12.16.1",
                          "12.15.1",
                          "12.14.1",
                          "12.13.1",
                          "12.12.1",
                          "12.11.1",
                          "12.10.1"
                        ]
                      },
                      "games_count": 5,
                      "games_lost": 2,
                      "games_won": 3,
                      "most_used_items": [
                        {
                          "count": 5,
                          "id": 2901,
                          "name": "Hextech Rocketbelt"
                        },
                        {
                          "count": 5,
                          "id": 2679,
                          "name": "Oracle Lens"
                        },
                        {
                          "count": 5,
                          "id": 2651,
                          "name": "Sorcerer's Shoes"
                        },
                        {
                          "count": 3,
                          "id": 2909,
                          "name": "Shadowflame"
                        },
                        {
                          "count": 3,
                          "id": 2467,
                          "name": "Dark Seal"
                        }
                      ]
                    },
                    {
                      "champion": {
                        "armor": 23,
                        "armorperlevel": 5.2,
                        "attackdamage": 53,
                        "attackdamageperlevel": 3,
                        "attackrange": 525,
                        "attackspeedoffset": null,
                        "attackspeedperlevel": 2.11,
                        "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/f4386b8f7a757ef7fdf2fa19dab0d6b6.jpg",
                        "crit": 0,
                        "critperlevel": 0,
                        "hp": 600,
                        "hpperlevel": 104,
                        "hpregen": 8,
                        "hpregenperlevel": 0.65,
                        "id": 3121,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/1a602e7dc475be3ca9ccba41689c71d3.png",
                        "movespeed": 335,
                        "mp": 405,
                        "mpperlevel": 45,
                        "mpregen": 8,
                        "mpregenperlevel": 0.8,
                        "name": "Viktor",
                        "slug": "Viktor",
                        "spellblock": 30,
                        "spellblockperlevel": 1.3,
                        "videogame_versions": [
                          "14.18.1",
                          "14.17.1",
                          "14.16.1",
                          "14.15.1",
                          "14.14.1",
                          "14.13.1",
                          "14.12.1",
                          "14.11.1",
                          "14.10.1",
                          "14.9.1",
                          "14.8.1",
                          "14.7.1",
                          "14.6.1",
                          "14.5.1",
                          "14.4.1",
                          "14.3.1",
                          "14.2.1",
                          "14.1.1",
                          "13.24.1",
                          "13.23.1",
                          "13.22.1",
                          "13.21.1",
                          "13.20.1",
                          "13.19.1",
                          "13.18.1",
                          "13.17.1",
                          "13.16.1",
                          "13.15.1",
                          "13.14.1",
                          "13.13.1",
                          "13.12.1",
                          "13.11.1",
                          "13.10.1",
                          "13.9.1",
                          "13.8.1",
                          "13.7.1",
                          "13.6.1",
                          "13.5.1",
                          "13.4.1",
                          "13.3.1",
                          "13.1.1",
                          "12.23.1",
                          "12.22.1",
                          "12.21.1",
                          "12.20.1",
                          "12.19.1",
                          "12.18.1",
                          "12.17.1",
                          "12.16.1",
                          "12.15.1",
                          "12.14.1",
                          "12.13.1",
                          "12.12.1",
                          "12.11.1",
                          "12.10.1"
                        ]
                      },
                      "games_count": 4,
                      "games_lost": 2,
                      "games_won": 2,
                      "most_used_items": [
                        {
                          "count": 4,
                          "id": 2923,
                          "name": "Lich Bane"
                        },
                        {
                          "count": 3,
                          "id": 3048,
                          "name": "Zhonya's Hourglass"
                        },
                        {
                          "count": 3,
                          "id": 2898,
                          "name": "Void Staff"
                        },
                        {
                          "count": 3,
                          "id": 2678,
                          "name": "Farsight Alteration"
                        },
                        {
                          "count": 2,
                          "id": 2908,
                          "name": "Crown of the Shattered Queen"
                        }
                      ]
                    },
                    {
                      "champion": {
                        "armor": 19,
                        "armorperlevel": 4.2,
                        "attackdamage": 52,
                        "attackdamageperlevel": 2.8,
                        "attackrange": 525,
                        "attackspeedoffset": null,
                        "attackspeedperlevel": 3,
                        "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/d66c97dc7f0c4e92e2de798ffe4969b9.jpg",
                        "crit": 0,
                        "critperlevel": 0,
                        "hp": 622,
                        "hpperlevel": 119,
                        "hpregen": 7,
                        "hpregenperlevel": 0.75,
                        "id": 2991,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/baf32ee97457437ea20c42ba23003e0c.png",
                        "movespeed": 335,
                        "mp": 480,
                        "mpperlevel": 21,
                        "mpregen": 8,
                        "mpregenperlevel": 0.8,
                        "name": "Azir",
                        "slug": "Azir",
                        "spellblock": 30,
                        "spellblockperlevel": 1.3,
                        "videogame_versions": [
                          "13.3.1",
                          "13.1.1",
                          "12.23.1",
                          "12.22.1",
                          "12.21.1",
                          "12.20.1",
                          "12.19.1",
                          "12.18.1",
                          "12.17.1",
                          "12.16.1",
                          "12.15.1",
                          "12.14.1",
                          "12.13.1",
                          "12.12.1",
                          "12.11.1",
                          "12.10.1"
                        ]
                      },
                      "games_count": 3,
                      "games_lost": 0,
                      "games_won": 3,
                      "most_used_items": [
                        {
                          "count": 3,
                          "id": 2898,
                          "name": "Void Staff"
                        },
                        {
                          "count": 3,
                          "id": 2678,
                          "name": "Farsight Alteration"
                        },
                        {
                          "count": 3,
                          "id": 2651,
                          "name": "Sorcerer's Shoes"
                        },
                        {
                          "count": 2,
                          "id": 2871,
                          "name": "Liandry's Anguish"
                        },
                        {
                          "count": 1,
                          "id": 3044,
                          "name": "Broken Stopwatch"
                        }
                      ]
                    },
                    {
                      "champion": {
                        "armor": 27,
                        "armorperlevel": 5.2,
                        "attackdamage": 61,
                        "attackdamageperlevel": 3,
                        "attackrange": 175,
                        "attackspeedoffset": null,
                        "attackspeedperlevel": 3.5,
                        "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/50891667-e2ed-4afe-a471-35e8d4716e76.jpg",
                        "crit": 0,
                        "critperlevel": 0,
                        "hp": 575,
                        "hpperlevel": 129,
                        "hpregen": 9,
                        "hpregenperlevel": 0.9,
                        "id": 3185,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/73d079e4-ba42-48a1-8a29-dae7f95b9587.png",
                        "movespeed": 340,
                        "mp": 310,
                        "mpperlevel": 70,
                        "mpregen": 8,
                        "mpregenperlevel": 0.8,
                        "name": "Sylas",
                        "slug": "Sylas",
                        "spellblock": 32,
                        "spellblockperlevel": 2.55,
                        "videogame_versions": [
                          "13.15.1",
                          "13.14.1",
                          "13.13.1",
                          "13.12.1",
                          "13.11.1",
                          "13.10.1",
                          "13.9.1",
                          "13.8.1",
                          "13.7.1",
                          "13.6.1",
                          "13.5.1",
                          "13.4.1",
                          "13.3.1",
                          "13.1.1",
                          "12.23.1",
                          "12.22.1",
                          "12.21.1",
                          "12.20.1",
                          "12.19.1",
                          "12.18.1",
                          "12.17.1"
                        ]
                      },
                      "games_count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "most_used_items": [
                        {
                          "count": 2,
                          "id": 2910,
                          "name": "Everfrost"
                        },
                        {
                          "count": 2,
                          "id": 2832,
                          "name": "Ionian Boots of Lucidity"
                        },
                        {
                          "count": 2,
                          "id": 2679,
                          "name": "Oracle Lens"
                        },
                        {
                          "count": 1,
                          "id": 3049,
                          "name": "Seeker's Armguard"
                        },
                        {
                          "count": 1,
                          "id": 3048,
                          "name": "Zhonya's Hourglass"
                        }
                      ]
                    },
                    {
                      "champion": {
                        "armor": 22,
                        "armorperlevel": 4.2,
                        "attackdamage": 58,
                        "attackdamageperlevel": 3,
                        "attackrange": 550,
                        "attackspeedoffset": null,
                        "attackspeedperlevel": 2.112,
                        "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/70cf425231ba194f2b9901c27d698847.jpg",
                        "crit": 0,
                        "critperlevel": 0,
                        "hp": 645,
                        "hpperlevel": 124,
                        "hpregen": 8,
                        "hpregenperlevel": 0.8,
                        "id": 3083,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/68910395988327ea8294bc5e36da5e96.png",
                        "movespeed": 340,
                        "mp": 300,
                        "mpperlevel": 70,
                        "mpregen": 8,
                        "mpregenperlevel": 1,
                        "name": "Ryze",
                        "slug": "Ryze",
                        "spellblock": 36,
                        "spellblockperlevel": 1.3,
                        "videogame_versions": [
                          "12.20.1",
                          "12.19.1",
                          "12.18.1",
                          "12.17.1",
                          "12.16.1",
                          "12.15.1",
                          "12.14.1",
                          "12.13.1",
                          "12.12.1",
                          "12.11.1",
                          "12.10.1"
                        ]
                      },
                      "games_count": 2,
                      "games_lost": 0,
                      "games_won": 2,
                      "most_used_items": [
                        {
                          "count": 2,
                          "id": 3048,
                          "name": "Zhonya's Hourglass"
                        },
                        {
                          "count": 2,
                          "id": 2919,
                          "name": "Seraph's Embrace"
                        },
                        {
                          "count": 2,
                          "id": 2910,
                          "name": "Everfrost"
                        },
                        {
                          "count": 2,
                          "id": 2814,
                          "name": "Rabadon's Deathcap"
                        },
                        {
                          "count": 2,
                          "id": 2679,
                          "name": "Oracle Lens"
                        }
                      ]
                    }
                  ],
                  "first_name": "Lee",
                  "id": 585,
                  "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                  "last_games": [
                    {
                      "assists": 4,
                      "champion": {
                        "id": 3121,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/1a602e7dc475be3ca9ccba41689c71d3.png",
                        "name": "Viktor",
                        "slug": "Viktor"
                      },
                      "creep_score": 325,
                      "cs_at_14": 124,
                      "deaths": 5,
                      "flags": {
                        "first_blood_assist": true,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 239290,
                      "gold_earned": 15380,
                      "gold_spent": 14925,
                      "items": [
                        {
                          "id": 2474,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                          "is_trinket": false,
                          "name": "Control Ward"
                        },
                        {
                          "id": 2678,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                          "is_trinket": true,
                          "name": "Farsight Alteration"
                        },
                        {
                          "id": 2832,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                          "is_trinket": false,
                          "name": "Ionian Boots of Lucidity"
                        },
                        {
                          "id": 2872,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/28a5336738db9b68b288d7796243eb33.png",
                          "is_trinket": false,
                          "name": "Luden's Tempest"
                        },
                        {
                          "id": 2898,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                          "is_trinket": false,
                          "name": "Void Staff"
                        },
                        {
                          "id": 2923,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/f0afeb951bcd89aa997e963f075bae83.png",
                          "is_trinket": false,
                          "name": "Lich Bane"
                        },
                        {
                          "id": 3048,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/e8bca3b0-24da-479e-9fa7-13f2021cc106.png",
                          "is_trinket": false,
                          "name": "Zhonya's Hourglass"
                        }
                      ],
                      "kills": 2,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 24,
                        "neutral_minions_enemy_jungle": 2,
                        "neutral_minions_team_jungle": 21,
                        "players": 2,
                        "turrets": 1,
                        "wards": 10
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
                      "level": 18,
                      "magic_damage": {
                        "dealt": 236647,
                        "dealt_to_champions": 21696,
                        "taken": 10507
                      },
                      "masteries": [],
                      "minions_killed": 325,
                      "opponent": {
                        "acronym": "DRX",
                        "dark_mode_image_url": null,
                        "id": 126370,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                        "location": "KR",
                        "modified_at": "2025-07-30T07:59:19Z",
                        "name": "DRX",
                        "slug": "dragonx"
                      },
                      "physical_damage": {
                        "dealt": 12520,
                        "dealt_to_champions": 474,
                        "taken": 8535
                      },
                      "player": {
                        "active": true,
                        "age": 29,
                        "birthday": "1996-05-07",
                        "first_name": "Lee",
                        "id": 585,
                        "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                        "last_name": "Sang-hyeok",
                        "modified_at": "2025-09-24T08:31:48Z",
                        "name": "Faker",
                        "nationality": "KR",
                        "role": "mid",
                        "slug": "faker"
                      },
                      "player_id": 585,
                      "role": "mid",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 5,
                          "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                          "keystone": {
                            "id": 52,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/fbe3405d6a68d3b7ae3f305fdf129e99.png",
                            "name": "Summon Aery",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 56,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                              "name": "Manaflow Band",
                              "type": "slot1"
                            },
                            {
                              "id": 58,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/632a47c2a88802029838e383a866feb1.png",
                              "name": "Transcendence",
                              "type": "slot2"
                            },
                            {
                              "id": 61,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                              "name": "Scorch",
                              "type": "slot3"
                            }
                          ],
                          "name": "Sorcery",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 4,
                          "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                          "lesser_runes": [
                            {
                              "id": 45,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/592200e1a39d2281977fc92d788cacd1.png",
                              "name": "Shield Bash",
                              "type": "slot1"
                            },
                            {
                              "id": 48,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/6054dc49089750c7d576b8e157228f29.png",
                              "name": "Bone Plating",
                              "type": "slot2"
                            }
                          ],
                          "name": "Resolve",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 68,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                            "name": "Magic Resist",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 69,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                            "name": "Attack Speed",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 39,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                          "name": "Teleport"
                        }
                      ],
                      "team": {
                        "acronym": "T1",
                        "dark_mode_image_url": null,
                        "id": 126061,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                        "location": "KR",
                        "modified_at": "2025-09-24T08:31:48Z",
                        "name": "T1",
                        "slug": "t1"
                      },
                      "total_damage": {
                        "dealt": 266474,
                        "dealt_to_champions": 22454,
                        "taken": 20289
                      },
                      "total_heal": 1294,
                      "total_time_crowd_control_dealt": 473,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 17307,
                        "dealt_to_champions": 284,
                        "taken": 1246
                      },
                      "wards": {
                        "placed": 21,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 14
                      },
                      "wards_placed": 21
                    },
                    {
                      "assists": 0,
                      "champion": {
                        "id": 2982,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/254171517c5418e10285bba695dfa951.png",
                        "name": "Akali",
                        "slug": "Akali"
                      },
                      "creep_score": 236,
                      "cs_at_14": 131,
                      "deaths": 3,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 239289,
                      "gold_earned": 9302,
                      "gold_spent": 9150,
                      "items": [
                        {
                          "id": 2474,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                          "is_trinket": false,
                          "name": "Control Ward"
                        },
                        {
                          "id": 2640,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/178aee5eaa5e7a70f6a05155b7dcf3e2.png",
                          "is_trinket": false,
                          "name": "Doran's Shield"
                        },
                        {
                          "id": 2651,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                          "is_trinket": false,
                          "name": "Sorcerer's Shoes"
                        },
                        {
                          "id": 2679,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                          "is_trinket": true,
                          "name": "Oracle Lens"
                        },
                        {
                          "id": 2901,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/e5f1a636a1edba83ccd1d7a48cb2cea2.png",
                          "is_trinket": false,
                          "name": "Hextech Rocketbelt"
                        },
                        {
                          "id": 2909,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/7ec8f413ab83b109852d5c3fd7c5b197.png",
                          "is_trinket": false,
                          "name": "Shadowflame"
                        },
                        {
                          "id": 3043,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/3c9dee81-cfff-4920-87ad-e0516ac0fc92.png",
                          "is_trinket": false,
                          "name": "Stopwatch"
                        }
                      ],
                      "kills": 0,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 4,
                        "neutral_minions_enemy_jungle": 0,
                        "neutral_minions_team_jungle": 4,
                        "players": 0,
                        "turrets": 0,
                        "wards": 8
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
                      "level": 14,
                      "magic_damage": {
                        "dealt": 100520,
                        "dealt_to_champions": 7742,
                        "taken": 12935
                      },
                      "masteries": [],
                      "minions_killed": 236,
                      "opponent": {
                        "acronym": "DRX",
                        "dark_mode_image_url": null,
                        "id": 126370,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                        "location": "KR",
                        "modified_at": "2025-07-30T07:59:19Z",
                        "name": "DRX",
                        "slug": "dragonx"
                      },
                      "physical_damage": {
                        "dealt": 16623,
                        "dealt_to_champions": 800,
                        "taken": 13599
                      },
                      "player": {
                        "active": true,
                        "age": 29,
                        "birthday": "1996-05-07",
                        "first_name": "Lee",
                        "id": 585,
                        "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                        "last_name": "Sang-hyeok",
                        "modified_at": "2025-09-24T08:31:48Z",
                        "name": "Faker",
                        "nationality": "KR",
                        "role": "mid",
                        "slug": "faker"
                      },
                      "player_id": 585,
                      "role": "mid",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 3,
                          "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                          "keystone": {
                            "id": 29,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d7dee9f79afc995429521e2b586aae87.png",
                            "name": "Fleet Footwork",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 33,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                              "name": "Presence of Mind",
                              "type": "slot1"
                            },
                            {
                              "id": 35,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                              "name": "Legend: Tenacity",
                              "type": "slot2"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                              "name": "Last Stand",
                              "type": "slot3"
                            }
                          ],
                          "name": "Precision",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 4,
                          "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                          "lesser_runes": [
                            {
                              "id": 47,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                              "name": "Second Wind",
                              "type": "slot2"
                            },
                            {
                              "id": 49,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
                              "name": "Overgrowth",
                              "type": "slot3"
                            }
                          ],
                          "name": "Resolve",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 68,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                            "name": "Magic Resist",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 68,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                            "name": "Magic Resist",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 71,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 39,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                          "name": "Teleport"
                        }
                      ],
                      "team": {
                        "acronym": "T1",
                        "dark_mode_image_url": null,
                        "id": 126061,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                        "location": "KR",
                        "modified_at": "2025-09-24T08:31:48Z",
                        "name": "T1",
                        "slug": "t1"
                      },
                      "total_damage": {
                        "dealt": 117583,
                        "dealt_to_champions": 8982,
                        "taken": 26904
                      },
                      "total_heal": 1759,
                      "total_time_crowd_control_dealt": 75,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 439,
                        "dealt_to_champions": 439,
                        "taken": 370
                      },
                      "wards": {
                        "placed": 8,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 6
                      },
                      "wards_placed": 8
                    },
                    {
                      "assists": 1,
                      "champion": {
                        "id": 2991,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/baf32ee97457437ea20c42ba23003e0c.png",
                        "name": "Azir",
                        "slug": "Azir"
                      },
                      "creep_score": 252,
                      "cs_at_14": 137,
                      "deaths": 5,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 239288,
                      "gold_earned": 12707,
                      "gold_spent": 12650,
                      "items": [
                        {
                          "id": 2474,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                          "is_trinket": false,
                          "name": "Control Ward"
                        },
                        {
                          "id": 2642,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/d3c7dce8ed50a8553198bdefbacac855.png",
                          "is_trinket": false,
                          "name": "Needlessly Large Rod"
                        },
                        {
                          "id": 2651,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                          "is_trinket": false,
                          "name": "Sorcerer's Shoes"
                        },
                        {
                          "id": 2678,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                          "is_trinket": true,
                          "name": "Farsight Alteration"
                        },
                        {
                          "id": 2871,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/8cef60e74adf20cb8372afd4aa49cde9.png",
                          "is_trinket": false,
                          "name": "Liandry's Anguish"
                        },
                        {
                          "id": 2898,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                          "is_trinket": false,
                          "name": "Void Staff"
                        },
                        {
                          "id": 2909,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/7ec8f413ab83b109852d5c3fd7c5b197.png",
                          "is_trinket": false,
                          "name": "Shadowflame"
                        }
                      ],
                      "kills": 3,
                      "kills_counters": {
                        "inhibitors": 1,
                        "neutral_minions": 20,
                        "neutral_minions_enemy_jungle": 6,
                        "neutral_minions_team_jungle": 12,
                        "players": 3,
                        "turrets": 1,
                        "wards": 5
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
                      "level": 16,
                      "magic_damage": {
                        "dealt": 144733,
                        "dealt_to_champions": 20874,
                        "taken": 7957
                      },
                      "masteries": [],
                      "minions_killed": 252,
                      "opponent": {
                        "acronym": "DRX",
                        "dark_mode_image_url": null,
                        "id": 126370,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                        "location": "KR",
                        "modified_at": "2025-07-30T07:59:19Z",
                        "name": "DRX",
                        "slug": "dragonx"
                      },
                      "physical_damage": {
                        "dealt": 13194,
                        "dealt_to_champions": 884,
                        "taken": 10830
                      },
                      "player": {
                        "active": true,
                        "age": 29,
                        "birthday": "1996-05-07",
                        "first_name": "Lee",
                        "id": 585,
                        "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                        "last_name": "Sang-hyeok",
                        "modified_at": "2025-09-24T08:31:48Z",
                        "name": "Faker",
                        "nationality": "KR",
                        "role": "mid",
                        "slug": "faker"
                      },
                      "player_id": 585,
                      "role": "mid",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 3,
                          "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                          "keystone": {
                            "id": 30,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                            "name": "Conqueror",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 33,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                              "name": "Presence of Mind",
                              "type": "slot1"
                            },
                            {
                              "id": 34,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                              "name": "Legend: Alacrity",
                              "type": "slot2"
                            },
                            {
                              "id": 38,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                              "name": "Cut Down",
                              "type": "slot3"
                            }
                          ],
                          "name": "Precision",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 5,
                          "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                          "lesser_runes": [
                            {
                              "id": 56,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                              "name": "Manaflow Band",
                              "type": "slot1"
                            },
                            {
                              "id": 61,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                              "name": "Scorch",
                              "type": "slot3"
                            }
                          ],
                          "name": "Sorcery",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 68,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                            "name": "Magic Resist",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 69,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                            "name": "Attack Speed",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 39,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                          "name": "Teleport"
                        }
                      ],
                      "team": {
                        "acronym": "T1",
                        "dark_mode_image_url": null,
                        "id": 126061,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                        "location": "KR",
                        "modified_at": "2025-09-24T08:31:48Z",
                        "name": "T1",
                        "slug": "t1"
                      },
                      "total_damage": {
                        "dealt": 157927,
                        "dealt_to_champions": 21759,
                        "taken": 19600
                      },
                      "total_heal": 1681,
                      "total_time_crowd_control_dealt": 212,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 0,
                        "dealt_to_champions": 0,
                        "taken": 813
                      },
                      "wards": {
                        "placed": 18,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 10
                      },
                      "wards_placed": 18
                    },
                    {
                      "assists": 2,
                      "champion": {
                        "id": 3121,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/1a602e7dc475be3ca9ccba41689c71d3.png",
                        "name": "Viktor",
                        "slug": "Viktor"
                      },
                      "creep_score": 406,
                      "cs_at_14": 111,
                      "deaths": 5,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 239287,
                      "gold_earned": 19088,
                      "gold_spent": 18025,
                      "items": [
                        {
                          "id": 2678,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                          "is_trinket": true,
                          "name": "Farsight Alteration"
                        },
                        {
                          "id": 2814,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                          "is_trinket": false,
                          "name": "Rabadon's Deathcap"
                        },
                        {
                          "id": 2832,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                          "is_trinket": false,
                          "name": "Ionian Boots of Lucidity"
                        },
                        {
                          "id": 2898,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                          "is_trinket": false,
                          "name": "Void Staff"
                        },
                        {
                          "id": 2908,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/e6408582a9edbfc6d6896b3dc2631cd7.png",
                          "is_trinket": false,
                          "name": "Crown of the Shattered Queen"
                        },
                        {
                          "id": 2923,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/f0afeb951bcd89aa997e963f075bae83.png",
                          "is_trinket": false,
                          "name": "Lich Bane"
                        },
                        {
                          "id": 3048,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/e8bca3b0-24da-479e-9fa7-13f2021cc106.png",
                          "is_trinket": false,
                          "name": "Zhonya's Hourglass"
                        }
                      ],
                      "kills": 4,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 29,
                        "neutral_minions_enemy_jungle": 0,
                        "neutral_minions_team_jungle": 27,
                        "players": 4,
                        "turrets": 2,
                        "wards": 10
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
                      "level": 18,
                      "magic_damage": {
                        "dealt": 340173,
                        "dealt_to_champions": 41078,
                        "taken": 10312
                      },
                      "masteries": [],
                      "minions_killed": 406,
                      "opponent": {
                        "acronym": "DRX",
                        "dark_mode_image_url": null,
                        "id": 126370,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                        "location": "KR",
                        "modified_at": "2025-07-30T07:59:19Z",
                        "name": "DRX",
                        "slug": "dragonx"
                      },
                      "physical_damage": {
                        "dealt": 17306,
                        "dealt_to_champions": 1251,
                        "taken": 13584
                      },
                      "player": {
                        "active": true,
                        "age": 29,
                        "birthday": "1996-05-07",
                        "first_name": "Lee",
                        "id": 585,
                        "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                        "last_name": "Sang-hyeok",
                        "modified_at": "2025-09-24T08:31:48Z",
                        "name": "Faker",
                        "nationality": "KR",
                        "role": "mid",
                        "slug": "faker"
                      },
                      "player_id": 585,
                      "role": "mid",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 2,
                          "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                          "keystone": {
                            "id": 65,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/13598521aebb0be68b52982d46aa1b1c.png",
                            "name": "First Strike",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 20,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a32387cef55cc07757a3175348d9dff3.png",
                              "name": "Triple Tonic",
                              "type": "slot1"
                            },
                            {
                              "id": 23,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                              "name": "Biscuit Delivery",
                              "type": "slot2"
                            },
                            {
                              "id": 24,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                              "name": "Cosmic Insight",
                              "type": "slot3"
                            }
                          ],
                          "name": "Inspiration",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 5,
                          "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                          "lesser_runes": [
                            {
                              "id": 56,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                              "name": "Manaflow Band",
                              "type": "slot1"
                            },
                            {
                              "id": 61,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                              "name": "Scorch",
                              "type": "slot3"
                            }
                          ],
                          "name": "Sorcery",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 68,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                            "name": "Magic Resist",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 69,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                            "name": "Attack Speed",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 39,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                          "name": "Teleport"
                        }
                      ],
                      "team": {
                        "acronym": "T1",
                        "dark_mode_image_url": null,
                        "id": 126061,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                        "location": "KR",
                        "modified_at": "2025-09-24T08:31:48Z",
                        "name": "T1",
                        "slug": "t1"
                      },
                      "total_damage": {
                        "dealt": 367575,
                        "dealt_to_champions": 43895,
                        "taken": 24425
                      },
                      "total_heal": 4698,
                      "total_time_crowd_control_dealt": 573,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 10094,
                        "dealt_to_champions": 1564,
                        "taken": 528
                      },
                      "wards": {
                        "placed": 28,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 13
                      },
                      "wards_placed": 28
                    },
                    {
                      "assists": 4,
                      "champion": {
                        "id": 2991,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/baf32ee97457437ea20c42ba23003e0c.png",
                        "name": "Azir",
                        "slug": "Azir"
                      },
                      "creep_score": 306,
                      "cs_at_14": 138,
                      "deaths": 1,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": true,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 239286,
                      "gold_earned": 15006,
                      "gold_spent": 14125,
                      "items": [
                        {
                          "id": 2651,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                          "is_trinket": false,
                          "name": "Sorcerer's Shoes"
                        },
                        {
                          "id": 2678,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                          "is_trinket": true,
                          "name": "Farsight Alteration"
                        },
                        {
                          "id": 2814,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                          "is_trinket": false,
                          "name": "Rabadon's Deathcap"
                        },
                        {
                          "id": 2898,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/42f72f4c6456b10d1aea5ca68e8e2355.png",
                          "is_trinket": false,
                          "name": "Void Staff"
                        },
                        {
                          "id": 2908,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/e6408582a9edbfc6d6896b3dc2631cd7.png",
                          "is_trinket": false,
                          "name": "Crown of the Shattered Queen"
                        },
                        {
                          "id": 3012,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/67ee113a533a1e443672e237d45f0043.png",
                          "is_trinket": false,
                          "name": "Morellonomicon"
                        }
                      ],
                      "kills": 6,
                      "kills_counters": {
                        "inhibitors": 2,
                        "neutral_minions": 44,
                        "neutral_minions_enemy_jungle": 9,
                        "neutral_minions_team_jungle": 22,
                        "players": 6,
                        "turrets": 4,
                        "wards": 8
                      },
                      "kills_series": {
                        "double_kills": 0,
                        "penta_kills": 0,
                        "quadra_kills": 0,
                        "triple_kills": 0
                      },
                      "largest_critical_strike": 0,
                      "largest_killing_spree": 6,
                      "largest_multi_kill": 1,
                      "level": 18,
                      "magic_damage": {
                        "dealt": 210751,
                        "dealt_to_champions": 24869,
                        "taken": 4884
                      },
                      "masteries": [],
                      "minions_killed": 306,
                      "opponent": {
                        "acronym": "DRX",
                        "dark_mode_image_url": null,
                        "id": 126370,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126370/220px_dr_xlogo_square.png",
                        "location": "KR",
                        "modified_at": "2025-07-30T07:59:19Z",
                        "name": "DRX",
                        "slug": "dragonx"
                      },
                      "physical_damage": {
                        "dealt": 13981,
                        "dealt_to_champions": 1006,
                        "taken": 9670
                      },
                      "player": {
                        "active": true,
                        "age": 29,
                        "birthday": "1996-05-07",
                        "first_name": "Lee",
                        "id": 585,
                        "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                        "last_name": "Sang-hyeok",
                        "modified_at": "2025-09-24T08:31:48Z",
                        "name": "Faker",
                        "nationality": "KR",
                        "role": "mid",
                        "slug": "faker"
                      },
                      "player_id": 585,
                      "role": "mid",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 3,
                          "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                          "keystone": {
                            "id": 30,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/aefc7bda4b2d6549ef850c58a9888a9a.png",
                            "name": "Conqueror",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 33,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                              "name": "Presence of Mind",
                              "type": "slot1"
                            },
                            {
                              "id": 34,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/acbf363d31d30086d5f27ac65439f145.png",
                              "name": "Legend: Alacrity",
                              "type": "slot2"
                            },
                            {
                              "id": 38,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                              "name": "Cut Down",
                              "type": "slot3"
                            }
                          ],
                          "name": "Precision",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 5,
                          "image_url": "https://cdn.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                          "lesser_runes": [
                            {
                              "id": 56,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                              "name": "Manaflow Band",
                              "type": "slot1"
                            },
                            {
                              "id": 61,
                              "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                              "name": "Scorch",
                              "type": "slot3"
                            }
                          ],
                          "name": "Sorcery",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 68,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                            "name": "Magic Resist",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 69,
                            "image_url": "https://cdn.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                            "name": "Attack Speed",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 39,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                          "name": "Teleport"
                        }
                      ],
                      "team": {
                        "acronym": "T1",
                        "dark_mode_image_url": null,
                        "id": 126061,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                        "location": "KR",
                        "modified_at": "2025-09-24T08:31:48Z",
                        "name": "T1",
                        "slug": "t1"
                      },
                      "total_damage": {
                        "dealt": 228568,
                        "dealt_to_champions": 26017,
                        "taken": 15122
                      },
                      "total_heal": 3782,
                      "total_time_crowd_control_dealt": 261,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 3835,
                        "dealt_to_champions": 140,
                        "taken": 566
                      },
                      "wards": {
                        "placed": 19,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 9
                      },
                      "wards_placed": 19
                    }
                  ],
                  "last_name": "Sang-hyeok",
                  "modified_at": "2025-09-24T08:31:48Z",
                  "name": "Faker",
                  "nationality": "KR",
                  "role": "mid",
                  "slug": "faker",
                  "stats": {
                    "averages": {
                      "assists": 5.33,
                      "cs_at_14": 123.06,
                      "cs_diff_at_14": -3.28,
                      "deaths": 3.11,
                      "gold_earned": 12679.83,
                      "gold_percentage": 20.63,
                      "gold_spent": 11829.17,
                      "kill_counters": {
                        "inhibitors": 0.39,
                        "neutral_minions": 17.44,
                        "neutral_minions_enemy_jungle": 4.2,
                        "neutral_minions_team_jungle": 12.93,
                        "players": 3.39,
                        "turrets": 1.33,
                        "wards": 5.83
                      },
                      "kills": 3.39,
                      "magic_damage": {
                        "dealt": 159618.94,
                        "dealt_percentage": 63.84,
                        "dealt_to_champions": 18781.56,
                        "dealt_to_champions_percentage": 51.27,
                        "taken": 8314.83
                      },
                      "minions_killed": 251.94,
                      "physical_damage": {
                        "dealt": 12045.44,
                        "dealt_percentage": 2.55,
                        "dealt_to_champions": 677.61,
                        "dealt_to_champions_percentage": 1.9,
                        "taken": 10208.83
                      },
                      "total_damage": {
                        "dealt": 177779.33,
                        "dealt_percentage": 23,
                        "dealt_to_champions": 19832.44,
                        "dealt_to_champions_percentage": 24.54,
                        "taken": 19331.17
                      },
                      "total_heal": 2638.5,
                      "total_time_crowd_control_dealt": 215.83,
                      "total_units_healed": 1.11,
                      "true_damage": {
                        "dealt": 6114.17,
                        "dealt_percentage": 12.08,
                        "dealt_to_champions": 372.28,
                        "dealt_to_champions_percentage": 6.14,
                        "taken": 806.67
                      },
                      "vision_wards_bought_in_game": 7.83,
                      "wards_placed": 13.5
                    },
                    "games_count": 18,
                    "serie": {
                      "begin_at": "2022-09-28T22:00:00Z",
                      "end_at": "2022-11-06T05:25:00Z",
                      "full_name": "2022",
                      "id": 5065,
                      "league": {
                        "id": 297,
                        "image_url": "https://cdn.pandascore.co/images/league/image/297/worlds-png",
                        "modified_at": "2023-12-06T15:53:28Z",
                        "name": "Worlds",
                        "slug": "league-of-legends-world-championship",
                        "url": null
                      },
                      "league_id": 297,
                      "modified_at": "2022-11-08T16:14:11Z",
                      "name": null,
                      "season": null,
                      "slug": "league-of-legends-world-championship-2022",
                      "tournaments": [
                        {
                          "begin_at": "2022-09-28T22:00:00Z",
                          "country": null,
                          "detailed_stats": true,
                          "end_at": "2022-10-03T03:45:00Z",
                          "has_bracket": false,
                          "id": 8933,
                          "league_id": 297,
                          "live_supported": true,
                          "modified_at": "2022-11-08T16:14:11Z",
                          "name": "Play-In Group A",
                          "prizepool": null,
                          "region": null,
                          "serie_id": 5065,
                          "slug": "league-of-legends-world-championship-2022-play-in-group-a",
                          "tier": "s",
                          "type": null,
                          "winner_id": null,
                          "winner_type": "Team"
                        },
                        {
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
                        {
                          "begin_at": "2022-10-03T18:00:00Z",
                          "country": null,
                          "detailed_stats": true,
                          "end_at": "2022-10-05T00:32:00Z",
                          "has_bracket": true,
                          "id": 8960,
                          "league_id": 297,
                          "live_supported": true,
                          "modified_at": "2022-11-08T16:14:11Z",
                          "name": "Play-In Elimination",
                          "prizepool": null,
                          "region": null,
                          "serie_id": 5065,
                          "slug": "league-of-legends-world-championship-2022-play-in-elimination",
                          "tier": "s",
                          "type": null,
                          "winner_id": null,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-10-07T21:00:00Z",
                          "country": null,
                          "detailed_stats": true,
                          "end_at": "2022-10-14T00:13:00Z",
                          "has_bracket": false,
                          "id": 9045,
                          "league_id": 297,
                          "live_supported": true,
                          "modified_at": "2022-11-08T16:14:11Z",
                          "name": "Group A",
                          "prizepool": null,
                          "region": null,
                          "serie_id": 5065,
                          "slug": "league-of-legends-world-championship-2022-group-a",
                          "tier": "s",
                          "type": null,
                          "winner_id": null,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-10-07T22:00:00Z",
                          "country": null,
                          "detailed_stats": true,
                          "end_at": "2022-10-15T01:31:00Z",
                          "has_bracket": false,
                          "id": 9046,
                          "league_id": 297,
                          "live_supported": true,
                          "modified_at": "2022-11-08T16:14:11Z",
                          "name": "Group B",
                          "prizepool": null,
                          "region": null,
                          "serie_id": 5065,
                          "slug": "league-of-legends-world-championship-2022-group-b",
                          "tier": "s",
                          "type": null,
                          "winner_id": null,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-10-07T23:00:00Z",
                          "country": null,
                          "detailed_stats": true,
                          "end_at": "2022-10-17T01:40:00Z",
                          "has_bracket": false,
                          "id": 9048,
                          "league_id": 297,
                          "live_supported": true,
                          "modified_at": "2022-11-08T16:14:11Z",
                          "name": "Group D",
                          "prizepool": null,
                          "region": null,
                          "serie_id": 5065,
                          "slug": "league-of-legends-world-championship-2022-group-d",
                          "tier": "s",
                          "type": null,
                          "winner_id": null,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-10-08T21:00:00Z",
                          "country": null,
                          "detailed_stats": true,
                          "end_at": "2022-10-16T01:31:00Z",
                          "has_bracket": false,
                          "id": 9047,
                          "league_id": 297,
                          "live_supported": true,
                          "modified_at": "2022-11-08T16:14:11Z",
                          "name": "Group C",
                          "prizepool": null,
                          "region": null,
                          "serie_id": 5065,
                          "slug": "league-of-legends-world-championship-2022-group-c",
                          "tier": "s",
                          "type": null,
                          "winner_id": null,
                          "winner_type": "Team"
                        },
                        {
                          "begin_at": "2022-10-20T21:00:00Z",
                          "country": null,
                          "detailed_stats": true,
                          "end_at": "2022-11-06T05:25:00Z",
                          "has_bracket": true,
                          "id": 9049,
                          "league_id": 297,
                          "live_supported": true,
                          "modified_at": "2023-04-25T16:27:42Z",
                          "name": "Playoffs",
                          "prizepool": "2225000 United States Dollar",
                          "region": null,
                          "serie_id": 5065,
                          "slug": "league-of-legends-world-championship-2022-playoffs",
                          "tier": "s",
                          "type": null,
                          "winner_id": 126370,
                          "winner_type": "Team"
                        }
                      ],
                      "videogame": {
                        "id": 1,
                        "name": "LoL",
                        "slug": "league-of-legends"
                      },
                      "videogame_title": null,
                      "winner_id": 126370,
                      "winner_type": "Team",
                      "year": 2022
                    },
                    "totals": {
                      "assists": 96,
                      "deaths": 56,
                      "games_lost": 5,
                      "games_played": 18,
                      "games_won": 13,
                      "kill_counters": {
                        "inhibitors": 7,
                        "turrets": 24,
                        "wards": 105
                      },
                      "kills": 61,
                      "kills_series": {
                        "double_kills": 3,
                        "penta_kills": 0,
                        "quadra_kills": 0,
                        "triple_kills": 0
                      },
                      "matches_lost": 2,
                      "matches_played": 9,
                      "matches_won": 7,
                      "wards_placed": 243
                    }
                  },
                  "teams": [
                    {
                      "acronym": "SS",
                      "dark_mode_image_url": null,
                      "id": 69,
                      "image_url": "https://cdn.pandascore.co/images/team/image/69/snake-iqttt327.png",
                      "location": "CN",
                      "modified_at": "2020-03-08T01:01:35Z",
                      "name": "Snake Esports",
                      "slug": "snake"
                    },
                    {
                      "acronym": "SKT",
                      "dark_mode_image_url": null,
                      "id": 100,
                      "image_url": "https://cdn.pandascore.co/images/team/image/100/sktelecom-t1-3mpugoym.png",
                      "location": "KR",
                      "modified_at": "2019-11-04T14:43:19Z",
                      "name": "SK telecom T1",
                      "slug": "sktelecom-t1"
                    },
                    {
                      "acronym": "KR",
                      "dark_mode_image_url": null,
                      "id": 371,
                      "image_url": "https://cdn.pandascore.co/images/team/image/371/lck-allstars-7bislmau.png",
                      "location": null,
                      "modified_at": "2019-07-24T12:39:08Z",
                      "name": "Korea All-Stars",
                      "slug": "lck-allstars"
                    },
                    {
                      "acronym": "TFS",
                      "dark_mode_image_url": null,
                      "id": 373,
                      "image_url": "https://cdn.pandascore.co/images/team/image/373/team-fire-allstars-6n3jppjm.png",
                      "location": null,
                      "modified_at": "2019-03-09T08:14:46Z",
                      "name": "Fire All-Stars",
                      "slug": "fire-allstars"
                    },
                    {
                      "acronym": "TFA",
                      "dark_mode_image_url": null,
                      "id": 378,
                      "image_url": "https://cdn.pandascore.co/images/team/image/378/team-fire-assassins-fv9eb68o.png",
                      "location": null,
                      "modified_at": "2017-04-03T09:07:26Z",
                      "name": "Fire Assassins",
                      "slug": "fire-assassins"
                    },
                    {
                      "acronym": null,
                      "dark_mode_image_url": null,
                      "id": 35437,
                      "image_url": null,
                      "location": null,
                      "modified_at": "2018-12-03T14:06:43Z",
                      "name": "Captain Faker",
                      "slug": "2v2t3"
                    },
                    {
                      "acronym": "NBPA",
                      "dark_mode_image_url": null,
                      "id": 35525,
                      "image_url": null,
                      "location": null,
                      "modified_at": "2018-12-06T09:48:10Z",
                      "name": "Nexus Blitz Pro Team 1",
                      "slug": "nexus-blitz-team-1"
                    },
                    {
                      "acronym": "URFA",
                      "dark_mode_image_url": null,
                      "id": 35536,
                      "image_url": null,
                      "location": null,
                      "modified_at": "2019-12-06T00:20:42Z",
                      "name": "URF Team 1",
                      "slug": "urf-team-1"
                    },
                    {
                      "acronym": "EVS3",
                      "dark_mode_image_url": null,
                      "id": 35547,
                      "image_url": null,
                      "location": null,
                      "modified_at": "2018-12-09T02:14:10Z",
                      "name": "East Team 3",
                      "slug": "east-team-3"
                    },
                    {
                      "acronym": "KRWIN",
                      "dark_mode_image_url": null,
                      "id": 35551,
                      "image_url": null,
                      "location": null,
                      "modified_at": "2018-12-06T08:17:49Z",
                      "name": "Korea Team",
                      "slug": "korea-team"
                    },
                    {
                      "acronym": "Faker",
                      "dark_mode_image_url": null,
                      "id": 43242,
                      "image_url": null,
                      "location": null,
                      "modified_at": "2022-12-19T11:11:30Z",
                      "name": "Faker",
                      "slug": "faker"
                    },
                    {
                      "acronym": "T1",
                      "dark_mode_image_url": null,
                      "id": 126061,
                      "image_url": "https://cdn.pandascore.co/images/team/image/126061/t_oscq04.png",
                      "location": "KR",
                      "modified_at": "2025-09-24T08:31:48Z",
                      "name": "T1",
                      "slug": "t1"
                    },
                    {
                      "acronym": "LCK",
                      "dark_mode_image_url": null,
                      "id": 126604,
                      "image_url": null,
                      "location": null,
                      "modified_at": "2020-12-16T20:38:22Z",
                      "name": "LCK Allstars",
                      "slug": "lck-allstars-league-of-legends"
                    },
                    {
                      "acronym": "ASSB",
                      "dark_mode_image_url": null,
                      "id": 126617,
                      "image_url": null,
                      "location": null,
                      "modified_at": "2019-12-07T06:04:12Z",
                      "name": "Assassin Team B",
                      "slug": "assassin-team-b"
                    },
                    {
                      "acronym": "APTR",
                      "dark_mode_image_url": null,
                      "id": 126629,
                      "image_url": null,
                      "location": null,
                      "modified_at": "2019-12-08T03:05:44Z",
                      "name": "All Pro Team Red",
                      "slug": "all-pro-team-red"
                    },
                    {
                      "acronym": "TF",
                      "dark_mode_image_url": null,
                      "id": 132502,
                      "image_url": null,
                      "location": "KR",
                      "modified_at": "2023-02-01T09:08:34Z",
                      "name": "Team Faker",
                      "slug": "team-faker"
                    },
                    {
                      "acronym": "KOR",
                      "dark_mode_image_url": null,
                      "id": 133694,
                      "image_url": "https://cdn.pandascore.co/images/team/image/133694/south_korea__28_national_team_29logo_square.png",
                      "location": "KR",
                      "modified_at": "2023-09-26T06:53:40Z",
                      "name": "South Korea",
                      "slug": "south-korea-league-of-legends"
                    },
                    {
                      "acronym": "MID",
                      "dark_mode_image_url": null,
                      "id": 134135,
                      "image_url": null,
                      "location": "KR",
                      "modified_at": "2024-01-09T09:47:51Z",
                      "name": "Team MID",
                      "slug": "team-mid"
                    }
                  ]
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLStatsForPlayerBySerie"
            }
          }
        },
        "description": "Statistics of a League-of-Legends player by serie\n\nDeprecated fields:\n- last_games[].minions_killed\n"
      }
    },
    "schemas": {
      "LoLStatsForPlayerBySerie": {
        "additionalProperties": false,
        "deprecated": false,
        "description": "Player's aggregated statistics for a serie",
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
          "favorite_champions": {
            "items": {
              "additionalProperties": false,
              "deprecated": false,
              "description": "A player's most used champion",
              "properties": {
                "champion": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "armor": {
                      "minimum": 0,
                      "title": "LoLArmor",
                      "type": "number"
                    },
                    "armorperlevel": {
                      "minimum": 0,
                      "title": "LoLArmorPerLevel",
                      "type": "number"
                    },
                    "attackdamage": {
                      "minimum": 0,
                      "title": "LoLAttackDamage",
                      "type": "number"
                    },
                    "attackdamageperlevel": {
                      "minimum": 0,
                      "title": "LoLAttackDamagePerLevel",
                      "type": "number"
                    },
                    "attackrange": {
                      "minimum": 0,
                      "title": "LoLAttackRange",
                      "type": "number"
                    },
                    "attackspeedoffset": {
                      "deprecated": false,
                      "nullable": true,
                      "title": "LoLAttackSpeedOffset",
                      "type": "number"
                    },
                    "attackspeedperlevel": {
                      "minimum": 0,
                      "title": "LoLAttackSpeedPerLevel",
                      "type": "number"
                    },
                    "big_image_url": {
                      "format": "uri",
                      "title": "LoLChampionBigImageURL",
                      "type": "string"
                    },
                    "crit": {
                      "minimum": 0,
                      "title": "LoLCrit",
                      "type": "number"
                    },
                    "critperlevel": {
                      "minimum": 0,
                      "title": "LoLCritPerLevel",
                      "type": "number"
                    },
                    "hp": {
                      "minimum": 0,
                      "title": "LoLHP",
                      "type": "number"
                    },
                    "hpperlevel": {
                      "minimum": 0,
                      "title": "LoLHPPerLevel",
                      "type": "number"
                    },
                    "hpregen": {
                      "minimum": 0,
                      "title": "LoLHPRegen",
                      "type": "number"
                    },
                    "hpregenperlevel": {
                      "minimum": 0,
                      "title": "LoLHPRegenPerLevel",
                      "type": "number"
                    },
                    "id": {
                      "minimum": 1,
                      "title": "LoLChampionID",
                      "type": "integer"
                    },
                    "image_url": {
                      "format": "uri",
                      "title": "LoLChampionImageURL",
                      "type": "string"
                    },
                    "movespeed": {
                      "minimum": 0,
                      "title": "LoLMoveSpeed",
                      "type": "number"
                    },
                    "mp": {
                      "minimum": 0,
                      "title": "LoLMP",
                      "type": "number"
                    },
                    "mpperlevel": {
                      "minimum": 0,
                      "title": "LoLMPPerLevel",
                      "type": "number"
                    },
                    "mpregen": {
                      "minimum": 0,
                      "title": "LoLMPRegen",
                      "type": "number"
                    },
                    "mpregenperlevel": {
                      "minimum": 0,
                      "title": "LoLMPRegenPerLevel",
                      "type": "number"
                    },
                    "name": {
                      "title": "LoLChampionName",
                      "type": "string"
                    },
                    "slug": {
                      "description": "Human-readable identifier of the champion.",
                      "title": "LoLChampionSlug",
                      "type": "string"
                    },
                    "spellblock": {
                      "minimum": 0,
                      "title": "LoLMagicResist",
                      "type": "number"
                    },
                    "spellblockperlevel": {
                      "minimum": 0,
                      "title": "LoLMagicResistPerLevel",
                      "type": "number"
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
                    "armor",
                    "armorperlevel",
                    "attackdamage",
                    "attackdamageperlevel",
                    "attackrange",
                    "attackspeedoffset",
                    "attackspeedperlevel",
                    "big_image_url",
                    "crit",
                    "critperlevel",
                    "hp",
                    "hpperlevel",
                    "hpregen",
                    "hpregenperlevel",
                    "id",
                    "image_url",
                    "movespeed",
                    "mp",
                    "mpperlevel",
                    "mpregen",
                    "mpregenperlevel",
                    "name",
                    "slug",
                    "spellblock",
                    "spellblockperlevel",
                    "videogame_versions"
                  ],
                  "title": "LoLChampion",
                  "type": "object"
                },
                "games_count": {
                  "description": "Number of games",
                  "minimum": 0,
                  "title": "GameCount",
                  "type": "integer"
                },
                "games_lost": {
                  "description": "Number of games lost by the player on the given champion",
                  "type": "integer"
                },
                "games_won": {
                  "description": "Number of games won by the player on the given champion",
                  "type": "integer"
                },
                "most_used_items": {
                  "items": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "description": "An item used by a champion",
                    "properties": {
                      "count": {
                        "minimum": 0,
                        "title": "LoLUsedItemCount",
                        "type": "integer"
                      },
                      "id": {
                        "minimum": 1,
                        "title": "LoLItemID",
                        "type": "integer"
                      },
                      "name": {
                        "title": "LoLItemName",
                        "type": "string"
                      }
                    },
                    "required": [
                      "count",
                      "id",
                      "name"
                    ],
                    "title": "LoLUsedItem",
                    "type": "object"
                  },
                  "title": "LoLUsedItems",
                  "type": "array"
                }
              },
              "required": [
                "champion",
                "games_count",
                "games_lost",
                "games_won",
                "most_used_items"
              ],
              "title": "LoLFavoriteChampion",
              "type": "object"
            },
            "title": "LoLFavoriteChampions",
            "type": "array"
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
          "last_games": {
            "items": {
              "additionalProperties": false,
              "deprecated": false,
              "description": "Player's data for a Game",
              "properties": {
                "assists": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLAssistCount",
                  "type": "integer"
                },
                "champion": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "nullable": true,
                  "properties": {
                    "id": {
                      "minimum": 1,
                      "title": "LoLChampionID",
                      "type": "integer"
                    },
                    "image_url": {
                      "format": "uri",
                      "title": "LoLChampionImageURL",
                      "type": "string"
                    },
                    "name": {
                      "title": "LoLChampionName",
                      "type": "string"
                    },
                    "slug": {
                      "description": "Human-readable identifier of the champion.",
                      "title": "LoLChampionSlug",
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "image_url",
                    "name",
                    "slug"
                  ],
                  "title": "BaseLoLChampion",
                  "type": "object"
                },
                "creep_score": {
                  "deprecated": false,
                  "description": "The player's Creep Score (CS.)\n\nNB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.",
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLCreepScore",
                  "type": "integer"
                },
                "cs_at_14": {
                  "deprecated": false,
                  "description": "The player's Creep Score (CS.) at 14minutes",
                  "minimum": 0,
                  "nullable": true,
                  "title": "LolCreepScoreAt14",
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
                "game_id": {
                  "description": "LoL game ID",
                  "minimum": 1,
                  "title": "LoLGameID",
                  "type": "integer"
                },
                "gold_earned": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLGold",
                  "type": "integer"
                },
                "gold_spent": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLGold",
                  "type": "integer"
                },
                "items": {
                  "items": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "id": {
                        "minimum": 1,
                        "title": "LoLItemID",
                        "type": "integer"
                      },
                      "image_url": {
                        "deprecated": false,
                        "format": "uri",
                        "nullable": true,
                        "title": "LoLItemImageURL",
                        "type": "string"
                      },
                      "is_trinket": {
                        "deprecated": false,
                        "description": "Whether item is a trinket",
                        "nullable": true,
                        "title": "LoLItemIsTrinket",
                        "type": "boolean"
                      },
                      "name": {
                        "title": "LoLItemName",
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "image_url",
                      "is_trinket",
                      "name"
                    ],
                    "title": "BaseLoLItem",
                    "type": "object"
                  },
                  "title": "BaseLoLItems",
                  "type": "array"
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
                "level": {
                  "deprecated": false,
                  "minimum": 1,
                  "nullable": true,
                  "title": "LoLChampionLevel",
                  "type": "integer"
                },
                "magic_damage": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "dealt": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    },
                    "dealt_to_champions": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    },
                    "taken": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    }
                  },
                  "required": [
                    "dealt",
                    "dealt_to_champions",
                    "taken"
                  ],
                  "title": "LoLGamePlayerDamageForStats",
                  "type": "object"
                },
                "masteries": {
                  "items": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "id": {
                        "minimum": 1,
                        "title": "LoLMasteryID",
                        "type": "integer"
                      },
                      "name": {
                        "title": "LoLMasteryName",
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "name"
                    ],
                    "title": "LoLMastery",
                    "type": "object"
                  },
                  "title": "LoLMasteries",
                  "type": "array"
                },
                "minions_killed": {
                  "deprecated": true,
                  "description": "The player's Creep Score (CS.)",
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLMinionsKilled",
                  "type": "integer"
                },
                "opponent": {
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
                "physical_damage": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "dealt": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    },
                    "dealt_to_champions": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    },
                    "taken": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    }
                  },
                  "required": [
                    "dealt",
                    "dealt_to_champions",
                    "taken"
                  ],
                  "title": "LoLGamePlayerDamageForStats",
                  "type": "object"
                },
                "player": {
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
                "runes": {
                  "items": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "id": {
                        "minimum": 1,
                        "title": "LoLRuneID",
                        "type": "integer"
                      },
                      "name": {
                        "title": "LoLRuneName",
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "name"
                    ],
                    "title": "LoLRune",
                    "type": "object"
                  },
                  "title": "LoLRunes",
                  "type": "array"
                },
                "runes_reforged": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "primary_path": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "nullable": true,
                      "properties": {
                        "id": {
                          "description": "ID of the rune",
                          "minimum": 1,
                          "title": "LoLRuneReforgedID",
                          "type": "integer"
                        },
                        "image_url": {
                          "description": "URL to an image of the rune",
                          "format": "uri",
                          "title": "LoLRuneReforgedImageURL",
                          "type": "string"
                        },
                        "keystone": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "properties": {
                            "id": {
                              "description": "ID of the rune",
                              "minimum": 1,
                              "title": "LoLRuneReforgedID",
                              "type": "integer"
                            },
                            "image_url": {
                              "description": "URL to an image of the rune",
                              "format": "uri",
                              "title": "LoLRuneReforgedImageURL",
                              "type": "string"
                            },
                            "name": {
                              "description": "Name of the rune path",
                              "title": "LoLRuneReforgedName",
                              "type": "string"
                            },
                            "type": {
                              "enum": [
                                "keystone",
                                "path",
                                "shard",
                                "slot1",
                                "slot2",
                                "slot3"
                              ],
                              "title": "LoLRuneReforgedType",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "type"
                          ],
                          "title": "LoLRuneReforged",
                          "type": "object"
                        },
                        "lesser_runes": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "description": "ID of the rune",
                                "minimum": 1,
                                "title": "LoLRuneReforgedID",
                                "type": "integer"
                              },
                              "image_url": {
                                "description": "URL to an image of the rune",
                                "format": "uri",
                                "title": "LoLRuneReforgedImageURL",
                                "type": "string"
                              },
                              "name": {
                                "description": "Name of the rune path",
                                "title": "LoLRuneReforgedName",
                                "type": "string"
                              },
                              "type": {
                                "enum": [
                                  "keystone",
                                  "path",
                                  "shard",
                                  "slot1",
                                  "slot2",
                                  "slot3"
                                ],
                                "title": "LoLRuneReforgedType",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "image_url",
                              "name",
                              "type"
                            ],
                            "title": "LoLRuneReforged",
                            "type": "object"
                          },
                          "title": "LoLRunesReforged",
                          "type": "array"
                        },
                        "name": {
                          "description": "Name of the rune path",
                          "title": "LoLRuneReforgedName",
                          "type": "string"
                        },
                        "type": {
                          "enum": [
                            "keystone",
                            "path",
                            "shard",
                            "slot1",
                            "slot2",
                            "slot3"
                          ],
                          "title": "LoLRuneReforgedType",
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "image_url",
                        "keystone",
                        "lesser_runes",
                        "name",
                        "type"
                      ],
                      "title": "LoLPlayerPrimaryRunePath",
                      "type": "object"
                    },
                    "secondary_path": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "nullable": true,
                      "properties": {
                        "id": {
                          "description": "ID of the rune",
                          "minimum": 1,
                          "title": "LoLRuneReforgedID",
                          "type": "integer"
                        },
                        "image_url": {
                          "description": "URL to an image of the rune",
                          "format": "uri",
                          "title": "LoLRuneReforgedImageURL",
                          "type": "string"
                        },
                        "lesser_runes": {
                          "items": {
                            "additionalProperties": false,
                            "deprecated": false,
                            "properties": {
                              "id": {
                                "description": "ID of the rune",
                                "minimum": 1,
                                "title": "LoLRuneReforgedID",
                                "type": "integer"
                              },
                              "image_url": {
                                "description": "URL to an image of the rune",
                                "format": "uri",
                                "title": "LoLRuneReforgedImageURL",
                                "type": "string"
                              },
                              "name": {
                                "description": "Name of the rune path",
                                "title": "LoLRuneReforgedName",
                                "type": "string"
                              },
                              "type": {
                                "enum": [
                                  "keystone",
                                  "path",
                                  "shard",
                                  "slot1",
                                  "slot2",
                                  "slot3"
                                ],
                                "title": "LoLRuneReforgedType",
                                "type": "string"
                              }
                            },
                            "required": [
                              "id",
                              "image_url",
                              "name",
                              "type"
                            ],
                            "title": "LoLRuneReforged",
                            "type": "object"
                          },
                          "title": "LoLRunesReforged",
                          "type": "array"
                        },
                        "name": {
                          "description": "Name of the rune path",
                          "title": "LoLRuneReforgedName",
                          "type": "string"
                        },
                        "type": {
                          "enum": [
                            "keystone",
                            "path",
                            "shard",
                            "slot1",
                            "slot2",
                            "slot3"
                          ],
                          "title": "LoLRuneReforgedType",
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "image_url",
                        "lesser_runes",
                        "name",
                        "type"
                      ],
                      "title": "LoLPlayerSecondaryRunePath",
                      "type": "object"
                    },
                    "shards": {
                      "additionalProperties": false,
                      "deprecated": false,
                      "properties": {
                        "defense": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "nullable": true,
                          "properties": {
                            "id": {
                              "description": "ID of the rune",
                              "minimum": 1,
                              "title": "LoLRuneReforgedID",
                              "type": "integer"
                            },
                            "image_url": {
                              "description": "URL to an image of the rune",
                              "format": "uri",
                              "title": "LoLRuneReforgedImageURL",
                              "type": "string"
                            },
                            "name": {
                              "description": "Name of the rune path",
                              "title": "LoLRuneReforgedName",
                              "type": "string"
                            },
                            "type": {
                              "enum": [
                                "keystone",
                                "path",
                                "shard",
                                "slot1",
                                "slot2",
                                "slot3"
                              ],
                              "title": "LoLRuneReforgedType",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "type"
                          ],
                          "title": "LoLRuneReforged",
                          "type": "object"
                        },
                        "flex": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "nullable": true,
                          "properties": {
                            "id": {
                              "description": "ID of the rune",
                              "minimum": 1,
                              "title": "LoLRuneReforgedID",
                              "type": "integer"
                            },
                            "image_url": {
                              "description": "URL to an image of the rune",
                              "format": "uri",
                              "title": "LoLRuneReforgedImageURL",
                              "type": "string"
                            },
                            "name": {
                              "description": "Name of the rune path",
                              "title": "LoLRuneReforgedName",
                              "type": "string"
                            },
                            "type": {
                              "enum": [
                                "keystone",
                                "path",
                                "shard",
                                "slot1",
                                "slot2",
                                "slot3"
                              ],
                              "title": "LoLRuneReforgedType",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "type"
                          ],
                          "title": "LoLRuneReforged",
                          "type": "object"
                        },
                        "offense": {
                          "additionalProperties": false,
                          "deprecated": false,
                          "nullable": true,
                          "properties": {
                            "id": {
                              "description": "ID of the rune",
                              "minimum": 1,
                              "title": "LoLRuneReforgedID",
                              "type": "integer"
                            },
                            "image_url": {
                              "description": "URL to an image of the rune",
                              "format": "uri",
                              "title": "LoLRuneReforgedImageURL",
                              "type": "string"
                            },
                            "name": {
                              "description": "Name of the rune path",
                              "title": "LoLRuneReforgedName",
                              "type": "string"
                            },
                            "type": {
                              "enum": [
                                "keystone",
                                "path",
                                "shard",
                                "slot1",
                                "slot2",
                                "slot3"
                              ],
                              "title": "LoLRuneReforgedType",
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "image_url",
                            "name",
                            "type"
                          ],
                          "title": "LoLRuneReforged",
                          "type": "object"
                        }
                      },
                      "required": [
                        "defense",
                        "flex",
                        "offense"
                      ],
                      "title": "LoLPlayerRuneShards",
                      "type": "object"
                    }
                  },
                  "required": [
                    "primary_path",
                    "secondary_path",
                    "shards"
                  ],
                  "title": "LoLPlayerRunesReforged",
                  "type": "object"
                },
                "spells": {
                  "items": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "id": {
                        "minimum": 1,
                        "title": "LoLSpellID",
                        "type": "integer"
                      },
                      "image_url": {
                        "format": "uri",
                        "title": "LoLSpellImageURL",
                        "type": "string"
                      },
                      "name": {
                        "title": "LoLSpellName",
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "image_url",
                      "name"
                    ],
                    "title": "LoLSpell",
                    "type": "object"
                  },
                  "title": "LoLSpells",
                  "type": "array"
                },
                "team": {
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
                },
                "total_damage": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "dealt": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    },
                    "dealt_to_champions": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    },
                    "taken": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    }
                  },
                  "required": [
                    "dealt",
                    "dealt_to_champions",
                    "taken"
                  ],
                  "title": "LoLGamePlayerDamageForStats",
                  "type": "object"
                },
                "total_heal": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLTotalHeal",
                  "type": "integer"
                },
                "total_time_crowd_control_dealt": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLTotalTimeCrowdControlDealt",
                  "type": "integer"
                },
                "total_units_healed": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLTotalUnitsHealed",
                  "type": "integer"
                },
                "true_damage": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "dealt": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    },
                    "dealt_to_champions": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    },
                    "taken": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
                    }
                  },
                  "required": [
                    "dealt",
                    "dealt_to_champions",
                    "taken"
                  ],
                  "title": "LoLGamePlayerDamageForStats",
                  "type": "object"
                },
                "wards": {
                  "additionalProperties": false,
                  "deprecated": false,
                  "properties": {
                    "placed": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLWardsPlaced",
                      "type": "integer"
                    },
                    "sight_wards_bought_in_game": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLSightWards",
                      "type": "integer"
                    },
                    "vision_wards_bought_in_game": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLVisionWards",
                      "type": "integer"
                    }
                  },
                  "required": [
                    "placed",
                    "sight_wards_bought_in_game",
                    "vision_wards_bought_in_game"
                  ],
                  "title": "LoLWards",
                  "type": "object"
                },
                "wards_placed": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLWardsPlaced",
                  "type": "integer"
                }
              },
              "required": [
                "assists",
                "champion",
                "creep_score",
                "cs_at_14",
                "deaths",
                "flags",
                "game_id",
                "gold_earned",
                "gold_spent",
                "items",
                "kills",
                "kills_counters",
                "kills_series",
                "largest_critical_strike",
                "largest_killing_spree",
                "largest_multi_kill",
                "level",
                "magic_damage",
                "masteries",
                "minions_killed",
                "opponent",
                "physical_damage",
                "player",
                "player_id",
                "role",
                "runes",
                "runes_reforged",
                "spells",
                "team",
                "total_damage",
                "total_heal",
                "total_time_crowd_control_dealt",
                "total_units_healed",
                "true_damage",
                "wards",
                "wards_placed"
              ],
              "title": "LoLGamePlayerForStats",
              "type": "object"
            },
            "title": "LoLGamePlayersForStats",
            "type": "array"
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
          },
          "stats": {
            "additionalProperties": false,
            "deprecated": false,
            "description": "Player's statistics for a serie",
            "properties": {
              "averages": {
                "additionalProperties": false,
                "deprecated": false,
                "properties": {
                  "assists": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageAssists",
                    "type": "number"
                  },
                  "cs_at_14": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LolAverageCreepScoreAt14",
                    "type": "number"
                  },
                  "cs_diff_at_14": {
                    "deprecated": false,
                    "description": "Player CS difference compared to their lane opponent at the 14th minute in-game",
                    "nullable": true,
                    "title": "LolAverageCreepScoreDifferenceAt14",
                    "type": "number"
                  },
                  "deaths": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageDeaths",
                    "type": "number"
                  },
                  "gold_earned": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageGoldEarned",
                    "type": "number"
                  },
                  "gold_percentage": {
                    "deprecated": false,
                    "description": "Percentage of gold the player had compared to the total gold of the team",
                    "maximum": 100,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLPlayerGoldErnedPercentage",
                    "type": "number"
                  },
                  "gold_spent": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageGoldSpent",
                    "type": "number"
                  },
                  "kill_counters": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "inhibitors": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageInhibitorKills",
                        "type": "number"
                      },
                      "neutral_minions": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageNeutralMinionKills",
                        "type": "number"
                      },
                      "neutral_minions_enemy_jungle": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageMinionsEnemyJungleKills",
                        "type": "number"
                      },
                      "neutral_minions_team_jungle": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageMinionsTeamJungleKills",
                        "type": "number"
                      },
                      "players": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageKills",
                        "type": "number"
                      },
                      "turrets": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageTurretKills",
                        "type": "number"
                      },
                      "wards": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageWardKills",
                        "type": "number"
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
                    "title": "LoLAverageKillCounters",
                    "type": "object"
                  },
                  "kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageKills",
                    "type": "number"
                  },
                  "magic_damage": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "dealt": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealt",
                        "type": "number"
                      },
                      "dealt_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtPercentage",
                        "type": "number"
                      },
                      "dealt_to_champions": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampions",
                        "type": "number"
                      },
                      "dealt_to_champions_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampionsPercentage",
                        "type": "number"
                      },
                      "taken": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageTaken",
                        "type": "number"
                      }
                    },
                    "required": [
                      "dealt",
                      "dealt_percentage",
                      "dealt_to_champions",
                      "dealt_to_champions_percentage",
                      "taken"
                    ],
                    "title": "LoLAverageMagicDamage",
                    "type": "object"
                  },
                  "minions_killed": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageMinionsKilled",
                    "type": "number"
                  },
                  "physical_damage": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "dealt": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealt",
                        "type": "number"
                      },
                      "dealt_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtPercentage",
                        "type": "number"
                      },
                      "dealt_to_champions": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampions",
                        "type": "number"
                      },
                      "dealt_to_champions_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampionsPercentage",
                        "type": "number"
                      },
                      "taken": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageTaken",
                        "type": "number"
                      }
                    },
                    "required": [
                      "dealt",
                      "dealt_percentage",
                      "dealt_to_champions",
                      "dealt_to_champions_percentage",
                      "taken"
                    ],
                    "title": "LoLAveragePhysicalDamage",
                    "type": "object"
                  },
                  "total_damage": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "dealt": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealt",
                        "type": "number"
                      },
                      "dealt_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtPercentage",
                        "type": "number"
                      },
                      "dealt_to_champions": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampions",
                        "type": "number"
                      },
                      "dealt_to_champions_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampionsPercentage",
                        "type": "number"
                      },
                      "taken": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageTaken",
                        "type": "number"
                      }
                    },
                    "required": [
                      "dealt",
                      "dealt_percentage",
                      "dealt_to_champions",
                      "dealt_to_champions_percentage",
                      "taken"
                    ],
                    "title": "LoLAverageTotalDamage",
                    "type": "object"
                  },
                  "total_heal": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageTotalHeal",
                    "type": "number"
                  },
                  "total_time_crowd_control_dealt": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageTotalTimeCrowdControlDealt",
                    "type": "number"
                  },
                  "total_units_healed": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageTotalUnitsHealed",
                    "type": "number"
                  },
                  "true_damage": {
                    "additionalProperties": false,
                    "deprecated": false,
                    "properties": {
                      "dealt": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealt",
                        "type": "number"
                      },
                      "dealt_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtPercentage",
                        "type": "number"
                      },
                      "dealt_to_champions": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampions",
                        "type": "number"
                      },
                      "dealt_to_champions_percentage": {
                        "deprecated": false,
                        "description": "Percentage of damage dealt to champions the player had compared to the total damage of the team",
                        "maximum": 100,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageDealtToChampionsPercentage",
                        "type": "number"
                      },
                      "taken": {
                        "deprecated": false,
                        "minimum": 0,
                        "nullable": true,
                        "title": "LoLAverageDamageTaken",
                        "type": "number"
                      }
                    },
                    "required": [
                      "dealt",
                      "dealt_percentage",
                      "dealt_to_champions",
                      "dealt_to_champions_percentage",
                      "taken"
                    ],
                    "title": "LoLAverageTrueDamage",
                    "type": "object"
                  },
                  "vision_wards_bought_in_game": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageVisionWardsBoughtInGame",
                    "type": "number"
                  },
                  "wards_placed": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLAverageWardsPlaced",
                    "type": "number"
                  }
                },
                "required": [
                  "assists",
                  "cs_at_14",
                  "cs_diff_at_14",
                  "deaths",
                  "gold_earned",
                  "gold_percentage",
                  "gold_spent",
                  "kill_counters",
                  "kills",
                  "magic_damage",
                  "minions_killed",
                  "physical_damage",
                  "total_damage",
                  "total_heal",
                  "total_time_crowd_control_dealt",
                  "total_units_healed",
                  "true_damage",
                  "vision_wards_bought_in_game",
                  "wards_placed"
                ],
                "title": "LoLPlayerAverages",
                "type": "object"
              },
              "games_count": {
                "deprecated": false,
                "description": "Number of games",
                "minimum": 0,
                "nullable": true,
                "title": "GameCount",
                "type": "integer"
              },
              "serie": {
                "additionalProperties": false,
                "deprecated": false,
                "description": "A serie, an occurrence of a league event",
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
                  "tournaments": {
                    "items": {
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
                    "title": "BaseTournaments",
                    "type": "array"
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
                  "league",
                  "league_id",
                  "modified_at",
                  "name",
                  "season",
                  "slug",
                  "tournaments",
                  "videogame",
                  "videogame_title",
                  "winner_id",
                  "winner_type",
                  "year"
                ],
                "title": "Serie",
                "type": "object"
              },
              "totals": {
                "additionalProperties": false,
                "deprecated": false,
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
                  "games_lost": {
                    "deprecated": false,
                    "description": "Number of games",
                    "minimum": 0,
                    "nullable": true,
                    "title": "GameCount",
                    "type": "integer"
                  },
                  "games_played": {
                    "deprecated": false,
                    "description": "Number of games",
                    "minimum": 0,
                    "nullable": true,
                    "title": "GameCount",
                    "type": "integer"
                  },
                  "games_won": {
                    "deprecated": false,
                    "description": "Number of games",
                    "minimum": 0,
                    "nullable": true,
                    "title": "GameCount",
                    "type": "integer"
                  },
                  "kill_counters": {
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
                      "turrets",
                      "wards"
                    ],
                    "title": "LoLPlayerTotalKillCounters",
                    "type": "object"
                  },
                  "kills": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLKillCount",
                    "type": "integer"
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
                  "matches_lost": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "MatchCount",
                    "type": "integer"
                  },
                  "matches_played": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "MatchCount",
                    "type": "integer"
                  },
                  "matches_won": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "MatchCount",
                    "type": "integer"
                  },
                  "wards_placed": {
                    "deprecated": false,
                    "minimum": 0,
                    "nullable": true,
                    "title": "LoLWardsPlaced",
                    "type": "integer"
                  }
                },
                "required": [
                  "assists",
                  "deaths",
                  "games_lost",
                  "games_played",
                  "games_won",
                  "kill_counters",
                  "kills",
                  "kills_series",
                  "matches_lost",
                  "matches_played",
                  "matches_won",
                  "wards_placed"
                ],
                "title": "LoLPlayerStatsTotals",
                "type": "object"
              }
            },
            "required": [
              "averages",
              "games_count",
              "serie",
              "totals"
            ],
            "title": "LoLPlayerBySerieStat",
            "type": "object"
          },
          "teams": {
            "items": {
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
            },
            "title": "BaseTeams",
            "type": "array"
          }
        },
        "required": [
          "active",
          "age",
          "birthday",
          "current_team",
          "current_videogame",
          "favorite_champions",
          "first_name",
          "id",
          "image_url",
          "last_games",
          "last_name",
          "modified_at",
          "name",
          "nationality",
          "role",
          "slug",
          "stats",
          "teams"
        ],
        "title": "LoLStatsForPlayerBySerie",
        "type": "object"
      },
      "PlayerIDOrSlug": {
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
      },
      "SerieIDOrSlug": {
        "description": "A serie ID or slug",
        "oneOf": [
          {
            "minimum": 1,
            "title": "SerieID",
            "type": "integer"
          },
          {
            "minLength": 1,
            "pattern": "^[a-z0-9_-]+$",
            "title": "SerieSlug",
            "type": "string"
          }
        ],
        "title": "SerieIDOrSlug"
      },
      "VideogameVersionOrAll": {
        "description": "Possible values are `latest`, `all` or a specific version number.",
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
        ],
        "title": "VideogameVersionOrAll"
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
    "/lol/series/{serie_id_or_slug}/players/{player_id_or_slug}/stats": {
      "get": {
        "description": "Get detailed statistics of a given League-of-Legends player for the given serie\n> ℹ️  \n> \n> This endpoint is only available to customers with a historical or real-time data plan",
        "operationId": "get_lol_series_serieIdOrSlug_players_playerIdOrSlug_stats",
        "parameters": [
          {
            "description": "A serie ID or slug",
            "in": "path",
            "name": "serie_id_or_slug",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/SerieIDOrSlug"
            }
          },
          {
            "description": "A player ID or slug",
            "in": "path",
            "name": "player_id_or_slug",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/PlayerIDOrSlug"
            }
          },
          {
            "$ref": "#/components/parameters/GamesCount"
          },
          {
            "$ref": "#/components/parameters/LoLStatsSide"
          },
          {
            "$ref": "#/components/parameters/StatsVideogameVersion"
          },
          {
            "$ref": "#/components/parameters/StatsFrom"
          },
          {
            "$ref": "#/components/parameters/StatsTo"
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLStatsForPlayerBySerie"
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
        "summary": "Get stats for LoL player on serie",
        "tags": [
          "LoL stats"
        ],
        "x-pandascore-plan": "Historical plan",
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/series/{serie_id_or_slug}/players/{player_id_or_slug}/stats' \\\n     --header 'accept: application/json'\n",
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