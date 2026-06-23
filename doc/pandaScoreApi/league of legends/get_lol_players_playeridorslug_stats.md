> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get stats for LoL player

Get detailed statistics of a given League-of-Legends player
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
      "LoLStatsForPlayer": {
        "content": {
          "application/json": {
            "examples": {
              "/lol/players/585/stats?from=2022-02-23&to=2022-05-13": {
                "description": "/lol/players/585/stats?from=2022-02-23&to=2022-05-13",
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
                        "armor": 18,
                        "armorperlevel": 3.5,
                        "attackdamage": 53,
                        "attackdamageperlevel": 3,
                        "attackrange": 550,
                        "attackspeedoffset": null,
                        "attackspeedperlevel": 2,
                        "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/18bae60ed5105a0a90f4d11145eba0fa.jpg",
                        "crit": 0,
                        "critperlevel": 0,
                        "hp": 500,
                        "hpperlevel": 82,
                        "hpregen": 2.5,
                        "hpregenperlevel": 0.6,
                        "id": 2941,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/4979c17972899770e5199844b846875a.png",
                        "movespeed": 330,
                        "mp": 418,
                        "mpperlevel": 25,
                        "mpregen": 8,
                        "mpregenperlevel": 0.8,
                        "name": "Ahri",
                        "slug": "Ahri",
                        "spellblock": 30,
                        "spellblockperlevel": 0.5,
                        "videogame_versions": [
                          "12.9.1",
                          "12.8.1",
                          "12.7.1",
                          "12.6.1",
                          "12.5.1",
                          "12.4.1",
                          "12.3.1"
                        ]
                      },
                      "games_count": 8,
                      "games_lost": 0,
                      "games_won": 8,
                      "most_used_items": [
                        {
                          "count": 8,
                          "id": 2910,
                          "name": "Everfrost"
                        },
                        {
                          "count": 7,
                          "id": 2832,
                          "name": "Ionian Boots of Lucidity"
                        },
                        {
                          "count": 6,
                          "id": 2473,
                          "name": "Corrupting Potion"
                        },
                        {
                          "count": 5,
                          "id": 2679,
                          "name": "Oracle Lens"
                        },
                        {
                          "count": 4,
                          "id": 2814,
                          "name": "Rabadon's Deathcap"
                        }
                      ]
                    },
                    {
                      "champion": {
                        "armor": 22,
                        "armorperlevel": 3.5,
                        "attackdamage": 55,
                        "attackdamageperlevel": 3.5,
                        "attackrange": 525,
                        "attackspeedoffset": null,
                        "attackspeedperlevel": 1.4,
                        "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/1c99a859a72800b0a036b5f25115baae.jpg",
                        "crit": 0,
                        "critperlevel": 0,
                        "hp": 528,
                        "hpperlevel": 97,
                        "hpregen": 7.5,
                        "hpregenperlevel": 0.55,
                        "id": 2847,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/7b89c13a2fa68b30ea885b7ff7841176.png",
                        "movespeed": 340,
                        "mp": 334,
                        "mpperlevel": 50,
                        "mpregen": 6,
                        "mpregenperlevel": 0.8,
                        "name": "LeBlanc",
                        "slug": "Leblanc",
                        "spellblock": 30,
                        "spellblockperlevel": 0.5,
                        "videogame_versions": [
                          "12.9.1",
                          "12.8.1",
                          "12.7.1",
                          "12.6.1",
                          "12.5.1",
                          "12.4.1",
                          "12.3.1",
                          "12.2.1",
                          "12.1.1",
                          "11.24.1",
                          "11.23.1",
                          "11.22.1",
                          "11.21.1",
                          "11.20.1",
                          "11.19.1",
                          "11.18.1",
                          "11.17.1",
                          "11.16.1",
                          "11.15.1",
                          "11.14.1",
                          "11.13.1",
                          "11.12.1",
                          "11.11.1",
                          "11.10.1",
                          "11.9.1",
                          "11.8.1",
                          "11.7.1",
                          "11.6.1",
                          "11.5.1",
                          "11.4.1",
                          "11.3.1",
                          "11.2.1"
                        ]
                      },
                      "games_count": 7,
                      "games_lost": 0,
                      "games_won": 7,
                      "most_used_items": [
                        {
                          "count": 7,
                          "id": 2679,
                          "name": "Oracle Lens"
                        },
                        {
                          "count": 6,
                          "id": 2467,
                          "name": "Dark Seal"
                        },
                        {
                          "count": 5,
                          "id": 2898,
                          "name": "Void Staff"
                        },
                        {
                          "count": 5,
                          "id": 2473,
                          "name": "Corrupting Potion"
                        },
                        {
                          "count": 4,
                          "id": 2872,
                          "name": "Luden's Tempest"
                        }
                      ]
                    },
                    {
                      "champion": {
                        "armor": 23,
                        "armorperlevel": 3.25,
                        "attackdamage": 54,
                        "attackdamageperlevel": 2.75,
                        "attackrange": 550,
                        "attackspeedoffset": null,
                        "attackspeedperlevel": 1,
                        "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/bafc198226d365950157776f7d7a99cf.jpg",
                        "crit": 0,
                        "critperlevel": 0,
                        "hp": 520,
                        "hpperlevel": 90,
                        "hpregen": 6.5,
                        "hpregenperlevel": 0.6,
                        "id": 2925,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/6f70c5e6082978490b31caa085f463fa.png",
                        "movespeed": 335,
                        "mp": 490,
                        "mpperlevel": 32,
                        "mpregen": 6,
                        "mpregenperlevel": 0.8,
                        "name": "Vex",
                        "slug": "Vex",
                        "spellblock": 28,
                        "spellblockperlevel": 0.5,
                        "videogame_versions": [
                          "12.9.1",
                          "12.8.1",
                          "12.7.1",
                          "12.6.1",
                          "12.5.1",
                          "12.4.1",
                          "12.3.1",
                          "12.2.1",
                          "12.1.1",
                          "11.24.1",
                          "11.23.1",
                          "11.22.1",
                          "11.21.1",
                          "11.20.1",
                          "11.19.1"
                        ]
                      },
                      "games_count": 3,
                      "games_lost": 0,
                      "games_won": 3,
                      "most_used_items": [
                        {
                          "count": 3,
                          "id": 2910,
                          "name": "Everfrost"
                        },
                        {
                          "count": 3,
                          "id": 2679,
                          "name": "Oracle Lens"
                        },
                        {
                          "count": 3,
                          "id": 2473,
                          "name": "Corrupting Potion"
                        },
                        {
                          "count": 2,
                          "id": 2898,
                          "name": "Void Staff"
                        },
                        {
                          "count": 2,
                          "id": 2651,
                          "name": "Sorcerer's Shoes"
                        }
                      ]
                    },
                    {
                      "champion": {
                        "armor": 22,
                        "armorperlevel": 3,
                        "attackdamage": 58,
                        "attackdamageperlevel": 3,
                        "attackrange": 550,
                        "attackspeedoffset": null,
                        "attackspeedperlevel": 2.112,
                        "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/70cf425231ba194f2b9901c27d698847.jpg",
                        "crit": 0,
                        "critperlevel": 0,
                        "hp": 575,
                        "hpperlevel": 110,
                        "hpregen": 8,
                        "hpregenperlevel": 0.8,
                        "id": 2882,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/68910395988327ea8294bc5e36da5e96.png",
                        "movespeed": 340,
                        "mp": 300,
                        "mpperlevel": 70,
                        "mpregen": 8,
                        "mpregenperlevel": 1,
                        "name": "Ryze",
                        "slug": "Ryze",
                        "spellblock": 36,
                        "spellblockperlevel": 0.5,
                        "videogame_versions": [
                          "12.9.1",
                          "12.8.1",
                          "12.7.1",
                          "12.6.1",
                          "12.5.1",
                          "12.4.1",
                          "12.3.1",
                          "12.2.1",
                          "12.1.1",
                          "11.24.1",
                          "11.23.1",
                          "11.22.1",
                          "11.21.1",
                          "11.20.1",
                          "11.19.1",
                          "11.18.1",
                          "11.17.1",
                          "11.16.1",
                          "11.15.1",
                          "11.14.1",
                          "11.13.1",
                          "11.12.1",
                          "11.11.1"
                        ]
                      },
                      "games_count": 3,
                      "games_lost": 1,
                      "games_won": 2,
                      "most_used_items": [
                        {
                          "count": 3,
                          "id": 2910,
                          "name": "Everfrost"
                        },
                        {
                          "count": 3,
                          "id": 2897,
                          "name": "Fimbulwinter"
                        },
                        {
                          "count": 3,
                          "id": 2830,
                          "name": "Frozen Heart"
                        },
                        {
                          "count": 3,
                          "id": 2473,
                          "name": "Corrupting Potion"
                        },
                        {
                          "count": 2,
                          "id": 2895,
                          "name": "Aegis of the Legion"
                        }
                      ]
                    },
                    {
                      "champion": {
                        "armor": 28,
                        "armorperlevel": 3,
                        "attackdamage": 59,
                        "attackdamageperlevel": 2,
                        "attackrange": 525,
                        "attackspeedoffset": null,
                        "attackspeedperlevel": 1.8,
                        "big_image_url": "https://cdn.pandascore.co/images/lol/champion/big_image/6d07254ceaee120c1747781a9d11fce5.jpg",
                        "crit": 0,
                        "critperlevel": 0,
                        "hp": 600,
                        "hpperlevel": 88,
                        "hpregen": 3.5,
                        "hpregenperlevel": 0.55,
                        "id": 2676,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/add835084b5385c8929c49c77c86a9cd.png",
                        "movespeed": 335,
                        "mp": 344.88,
                        "mpperlevel": 38,
                        "mpregen": 8.2,
                        "mpregenperlevel": 0.45,
                        "name": "Kai'Sa",
                        "slug": "Kaisa",
                        "spellblock": 30,
                        "spellblockperlevel": 0.5,
                        "videogame_versions": [
                          "12.9.1",
                          "12.8.1",
                          "12.7.1",
                          "12.6.1",
                          "12.5.1",
                          "12.4.1",
                          "12.3.1",
                          "12.2.1",
                          "12.1.1",
                          "11.24.1",
                          "11.23.1",
                          "11.22.1",
                          "11.21.1",
                          "11.20.1",
                          "11.19.1",
                          "11.18.1",
                          "11.17.1",
                          "11.16.1",
                          "11.15.1",
                          "11.14.1",
                          "11.13.1",
                          "11.12.1",
                          "11.11.1",
                          "11.10.1",
                          "11.9.1",
                          "11.8.1",
                          "11.7.1",
                          "11.6.1",
                          "11.5.1",
                          "11.4.1",
                          "11.3.1",
                          "11.2.1",
                          "11.1.1",
                          "10.25.1",
                          "10.24.1",
                          "10.23.1",
                          "10.22.1",
                          "10.21.1",
                          "10.20.1",
                          "10.19.1",
                          "10.18.1"
                        ]
                      },
                      "games_count": 2,
                      "games_lost": 1,
                      "games_won": 1,
                      "most_used_items": [
                        {
                          "count": 2,
                          "id": 2872,
                          "name": "Luden's Tempest"
                        },
                        {
                          "count": 2,
                          "id": 2811,
                          "name": "Muramana"
                        },
                        {
                          "count": 2,
                          "id": 2678,
                          "name": "Farsight Alteration"
                        },
                        {
                          "count": 2,
                          "id": 2651,
                          "name": "Sorcerer's Shoes"
                        },
                        {
                          "count": 2,
                          "id": 2642,
                          "name": "Needlessly Large Rod"
                        }
                      ]
                    }
                  ],
                  "first_name": "Lee",
                  "id": 585,
                  "image_url": "https://cdn.pandascore.co/images/player/image/585/t1_faker_2023_split_2.png",
                  "last_games": [
                    {
                      "assists": 5,
                      "champion": {
                        "id": 2847,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/7b89c13a2fa68b30ea885b7ff7841176.png",
                        "name": "LeBlanc",
                        "slug": "Leblanc"
                      },
                      "creep_score": 171,
                      "cs_at_14": 113,
                      "deaths": 3,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 233584,
                      "gold_earned": 9902,
                      "gold_spent": 9725,
                      "items": [
                        {
                          "id": 2467,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/e914701535346c87ea1cfb1fb159631c.png",
                          "is_trinket": false,
                          "name": "Dark Seal"
                        },
                        {
                          "id": 2477,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/c5ee3255d75b989f677f7d622394df31.png",
                          "is_trinket": false,
                          "name": "Elixir of Sorcery"
                        },
                        {
                          "id": 2651,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/abbbe229a0d623874a20e209c5b50041.png",
                          "is_trinket": false,
                          "name": "Sorcerer's Shoes"
                        },
                        {
                          "id": 2660,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/c5709a137fafe955c32ae4511fb78d99.png",
                          "is_trinket": false,
                          "name": "Tear of the Goddess"
                        },
                        {
                          "id": 2679,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                          "is_trinket": true,
                          "name": "Oracle Lens"
                        },
                        {
                          "id": 2872,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/28a5336738db9b68b288d7796243eb33.png",
                          "is_trinket": false,
                          "name": "Luden's Tempest"
                        },
                        {
                          "id": 2909,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/7ec8f413ab83b109852d5c3fd7c5b197.png",
                          "is_trinket": false,
                          "name": "Shadowflame"
                        }
                      ],
                      "kills": 4,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 9,
                        "neutral_minions_enemy_jungle": null,
                        "neutral_minions_team_jungle": null,
                        "players": 4,
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
                      "largest_killing_spree": 2,
                      "largest_multi_kill": 1,
                      "level": 14,
                      "magic_damage": {
                        "dealt": 53131,
                        "dealt_to_champions": 10813,
                        "taken": 6093
                      },
                      "masteries": [],
                      "minions_killed": 171,
                      "opponent": {
                        "acronym": "DFM",
                        "dark_mode_image_url": null,
                        "id": 89,
                        "image_url": "https://cdn.pandascore.co/images/team/image/89/detonation-focusme-fpnjh4v7.png",
                        "location": "JP",
                        "modified_at": "2025-08-25T08:57:20Z",
                        "name": "DetonatioN FocusMe",
                        "slug": "detonation-focusme"
                      },
                      "physical_damage": {
                        "dealt": 15759,
                        "dealt_to_champions": 1221,
                        "taken": 7829
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
                        "primary_path": null,
                        "secondary_path": null,
                        "shards": {
                          "defense": null,
                          "flex": null,
                          "offense": null
                        }
                      },
                      "spells": [
                        {
                          "id": 26,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                          "name": "Ignite"
                        },
                        {
                          "id": 28,
                          "image_url": "https://cdn.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
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
                        "dealt": 69648,
                        "dealt_to_champions": 12793,
                        "taken": 15230
                      },
                      "total_heal": 2327,
                      "total_time_crowd_control_dealt": 23,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 758,
                        "dealt_to_champions": 758,
                        "taken": 1307
                      },
                      "wards": {
                        "placed": 25,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 9
                      },
                      "wards_placed": 25
                    },
                    {
                      "assists": 8,
                      "champion": {
                        "id": 2941,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/4979c17972899770e5199844b846875a.png",
                        "name": "Ahri",
                        "slug": "Ahri"
                      },
                      "creep_score": 200,
                      "cs_at_14": 136,
                      "deaths": 0,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": true,
                        "first_inhibitor_assist": true,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 233576,
                      "gold_earned": 10731,
                      "gold_spent": 9650,
                      "items": [
                        {
                          "id": 2473,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/7e869611bdd37522a83fb50079aadafb.png",
                          "is_trinket": false,
                          "name": "Corrupting Potion"
                        },
                        {
                          "id": 2499,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/95f8b2323890310c5d277d71551bc0e6.png",
                          "is_trinket": false,
                          "name": "Mejai's Soulstealer"
                        },
                        {
                          "id": 2534,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/73578d8f7a2a451b61696009016c134a.png",
                          "is_trinket": false,
                          "name": "Fiendish Codex"
                        },
                        {
                          "id": 2537,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                          "is_trinket": false,
                          "name": "Mercury's Treads"
                        },
                        {
                          "id": 2679,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                          "is_trinket": true,
                          "name": "Oracle Lens"
                        },
                        {
                          "id": 2776,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/000057177c6cd0f3895e67b2199dacb9.png",
                          "is_trinket": false,
                          "name": "Zhonya's Hourglass"
                        },
                        {
                          "id": 2910,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/a8377226b797197fdb941b2fad4123cb.png",
                          "is_trinket": false,
                          "name": "Everfrost"
                        }
                      ],
                      "kills": 7,
                      "kills_counters": {
                        "inhibitors": 1,
                        "neutral_minions": 6,
                        "neutral_minions_enemy_jungle": null,
                        "neutral_minions_team_jungle": null,
                        "players": 7,
                        "turrets": 0,
                        "wards": 8
                      },
                      "kills_series": {
                        "double_kills": 1,
                        "penta_kills": 0,
                        "quadra_kills": 0,
                        "triple_kills": 0
                      },
                      "largest_critical_strike": 0,
                      "largest_killing_spree": 7,
                      "largest_multi_kill": 2,
                      "level": 14,
                      "magic_damage": {
                        "dealt": 61909,
                        "dealt_to_champions": 8074,
                        "taken": 2196
                      },
                      "masteries": [],
                      "minions_killed": 200,
                      "opponent": {
                        "acronym": "AZE",
                        "dark_mode_image_url": null,
                        "id": 129487,
                        "image_url": "https://cdn.pandascore.co/images/team/image/129487/team_azelogo_square.png",
                        "location": "MX",
                        "modified_at": "2023-08-02T01:04:06Z",
                        "name": "Team Aze",
                        "slug": "team-aze"
                      },
                      "physical_damage": {
                        "dealt": 12862,
                        "dealt_to_champions": 1149,
                        "taken": 5855
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
                        "primary_path": null,
                        "secondary_path": null,
                        "shards": {
                          "defense": null,
                          "flex": null,
                          "offense": null
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
                        "dealt": 104723,
                        "dealt_to_champions": 12197,
                        "taken": 8052
                      },
                      "total_heal": 4307,
                      "total_time_crowd_control_dealt": 57,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 29951,
                        "dealt_to_champions": 2973,
                        "taken": 0
                      },
                      "wards": {
                        "placed": 13,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 2
                      },
                      "wards_placed": 13
                    },
                    {
                      "assists": 5,
                      "champion": {
                        "id": 2727,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/b9d51654c13fa168ada10500969316b1.png",
                        "name": "Twisted Fate",
                        "slug": "TwistedFate"
                      },
                      "creep_score": 201,
                      "cs_at_14": 131,
                      "deaths": 1,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 233567,
                      "gold_earned": 11299,
                      "gold_spent": 8725,
                      "items": [
                        {
                          "id": 2473,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/7e869611bdd37522a83fb50079aadafb.png",
                          "is_trinket": false,
                          "name": "Corrupting Potion"
                        },
                        {
                          "id": 2499,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/95f8b2323890310c5d277d71551bc0e6.png",
                          "is_trinket": false,
                          "name": "Mejai's Soulstealer"
                        },
                        {
                          "id": 2537,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                          "is_trinket": false,
                          "name": "Mercury's Treads"
                        },
                        {
                          "id": 2678,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                          "is_trinket": true,
                          "name": "Farsight Alteration"
                        },
                        {
                          "id": 2714,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/2e9e74676892b4fbaf86c33e959bf373.png",
                          "is_trinket": false,
                          "name": "Rapid Firecannon"
                        },
                        {
                          "id": 2910,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/a8377226b797197fdb941b2fad4123cb.png",
                          "is_trinket": false,
                          "name": "Everfrost"
                        }
                      ],
                      "kills": 2,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 12,
                        "neutral_minions_enemy_jungle": null,
                        "neutral_minions_team_jungle": null,
                        "players": 2,
                        "turrets": 3,
                        "wards": 1
                      },
                      "kills_series": {
                        "double_kills": 0,
                        "penta_kills": 0,
                        "quadra_kills": 0,
                        "triple_kills": 0
                      },
                      "largest_critical_strike": 193,
                      "largest_killing_spree": 2,
                      "largest_multi_kill": 1,
                      "level": 15,
                      "magic_damage": {
                        "dealt": 104631,
                        "dealt_to_champions": 11683,
                        "taken": 6564
                      },
                      "masteries": [],
                      "minions_killed": 201,
                      "opponent": {
                        "acronym": "SGB",
                        "dark_mode_image_url": null,
                        "id": 126073,
                        "image_url": "https://cdn.pandascore.co/images/team/image/126073/220px_saigon_buffalologo_square.png",
                        "location": "VN",
                        "modified_at": "2024-01-13T07:45:26Z",
                        "name": "Saigon Buffalo",
                        "slug": "dashing-buffalo"
                      },
                      "physical_damage": {
                        "dealt": 19375,
                        "dealt_to_champions": 2220,
                        "taken": 5181
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
                        "primary_path": null,
                        "secondary_path": null,
                        "shards": {
                          "defense": null,
                          "flex": null,
                          "offense": null
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
                        "dealt": 126864,
                        "dealt_to_champions": 14500,
                        "taken": 11863
                      },
                      "total_heal": 1776,
                      "total_time_crowd_control_dealt": 230,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 2858,
                        "dealt_to_champions": 596,
                        "taken": 118
                      },
                      "wards": {
                        "placed": 11,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 3
                      },
                      "wards_placed": 11
                    },
                    {
                      "assists": 6,
                      "champion": {
                        "id": 2941,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/4979c17972899770e5199844b846875a.png",
                        "name": "Ahri",
                        "slug": "Ahri"
                      },
                      "creep_score": 266,
                      "cs_at_14": 140,
                      "deaths": 0,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 232508,
                      "gold_earned": 12452,
                      "gold_spent": 12025,
                      "items": [
                        {
                          "id": 2473,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/7e869611bdd37522a83fb50079aadafb.png",
                          "is_trinket": false,
                          "name": "Corrupting Potion"
                        },
                        {
                          "id": 2481,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/84b0db5c9726c8bd47c9c8c088f6e8fb.png",
                          "is_trinket": false,
                          "name": "Broken Stopwatch"
                        },
                        {
                          "id": 2679,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                          "is_trinket": true,
                          "name": "Oracle Lens"
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
                          "id": 2904,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/2ead95b7f09377e9a3a0d38b77f4641c.png",
                          "is_trinket": false,
                          "name": "Horizon Focus"
                        },
                        {
                          "id": 2910,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/a8377226b797197fdb941b2fad4123cb.png",
                          "is_trinket": false,
                          "name": "Everfrost"
                        }
                      ],
                      "kills": 4,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 23,
                        "neutral_minions_enemy_jungle": null,
                        "neutral_minions_team_jungle": null,
                        "players": 4,
                        "turrets": 2,
                        "wards": 9
                      },
                      "kills_series": {
                        "double_kills": 0,
                        "penta_kills": 0,
                        "quadra_kills": 0,
                        "triple_kills": 0
                      },
                      "largest_critical_strike": 0,
                      "largest_killing_spree": 4,
                      "largest_multi_kill": 1,
                      "level": 16,
                      "magic_damage": {
                        "dealt": 94998,
                        "dealt_to_champions": 9901,
                        "taken": 3575
                      },
                      "masteries": [],
                      "minions_killed": 266,
                      "opponent": {
                        "acronym": "GEN",
                        "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/2882/499px_gen.g_esports_2019_full_darkmode.png",
                        "id": 2882,
                        "image_url": "https://cdn.pandascore.co/images/team/image/2882/500px_gen.g_esports_2019_full_lightmode.png",
                        "location": "KR",
                        "modified_at": "2025-09-24T08:57:42Z",
                        "name": "Gen.G",
                        "slug": "geng"
                      },
                      "physical_damage": {
                        "dealt": 18495,
                        "dealt_to_champions": 1122,
                        "taken": 7766
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
                        "primary_path": null,
                        "secondary_path": null,
                        "shards": {
                          "defense": null,
                          "flex": null,
                          "offense": null
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
                        "dealt": 159836,
                        "dealt_to_champions": 13085,
                        "taken": 11366
                      },
                      "total_heal": 5995,
                      "total_time_crowd_control_dealt": 50,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 46343,
                        "dealt_to_champions": 2061,
                        "taken": 25
                      },
                      "wards": {
                        "placed": 16,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 7
                      },
                      "wards_placed": 16
                    },
                    {
                      "assists": 8,
                      "champion": {
                        "id": 2941,
                        "image_url": "https://cdn.pandascore.co/images/lol/champion/image/4979c17972899770e5199844b846875a.png",
                        "name": "Ahri",
                        "slug": "Ahri"
                      },
                      "creep_score": 293,
                      "cs_at_14": 128,
                      "deaths": 0,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": true
                      },
                      "game_id": 232507,
                      "gold_earned": 13943,
                      "gold_spent": 13300,
                      "items": [
                        {
                          "id": 2447,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/93bb71d5aba94a73ab32a16bf3708869.png",
                          "is_trinket": false,
                          "name": "Blasting Wand"
                        },
                        {
                          "id": 2598,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/ff18cd0febe9580d5e5445fb32786b15.png",
                          "is_trinket": false,
                          "name": "Blighting Jewel"
                        },
                        {
                          "id": 2678,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                          "is_trinket": true,
                          "name": "Farsight Alteration"
                        },
                        {
                          "id": 2776,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/000057177c6cd0f3895e67b2199dacb9.png",
                          "is_trinket": false,
                          "name": "Zhonya's Hourglass"
                        },
                        {
                          "id": 2832,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                          "is_trinket": false,
                          "name": "Ionian Boots of Lucidity"
                        },
                        {
                          "id": 2904,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/2ead95b7f09377e9a3a0d38b77f4641c.png",
                          "is_trinket": false,
                          "name": "Horizon Focus"
                        },
                        {
                          "id": 2910,
                          "image_url": "https://cdn.pandascore.co/images/lol/item/image/a8377226b797197fdb941b2fad4123cb.png",
                          "is_trinket": false,
                          "name": "Everfrost"
                        }
                      ],
                      "kills": 0,
                      "kills_counters": {
                        "inhibitors": 1,
                        "neutral_minions": 33,
                        "neutral_minions_enemy_jungle": null,
                        "neutral_minions_team_jungle": null,
                        "players": 0,
                        "turrets": 3,
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
                      "largest_multi_kill": 0,
                      "level": 17,
                      "magic_damage": {
                        "dealt": 107631,
                        "dealt_to_champions": 8809,
                        "taken": 13232
                      },
                      "masteries": [],
                      "minions_killed": 293,
                      "opponent": {
                        "acronym": "GEN",
                        "dark_mode_image_url": "https://cdn.pandascore.co/dark_images/team/dark_image/2882/499px_gen.g_esports_2019_full_darkmode.png",
                        "id": 2882,
                        "image_url": "https://cdn.pandascore.co/images/team/image/2882/500px_gen.g_esports_2019_full_lightmode.png",
                        "location": "KR",
                        "modified_at": "2025-09-24T08:57:42Z",
                        "name": "Gen.G",
                        "slug": "geng"
                      },
                      "physical_damage": {
                        "dealt": 22562,
                        "dealt_to_champions": 1566,
                        "taken": 7820
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
                        "primary_path": null,
                        "secondary_path": null,
                        "shards": {
                          "defense": null,
                          "flex": null,
                          "offense": null
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
                        "dealt": 178830,
                        "dealt_to_champions": 12206,
                        "taken": 21467
                      },
                      "total_heal": 10724,
                      "total_time_crowd_control_dealt": 106,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 48636,
                        "dealt_to_champions": 1831,
                        "taken": 415
                      },
                      "wards": {
                        "placed": 23,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 6
                      },
                      "wards_placed": 23
                    }
                  ],
                  "last_name": "Sang-hyeok",
                  "modified_at": "2025-09-24T08:31:48Z",
                  "name": "Faker",
                  "nationality": "KR",
                  "role": "mid",
                  "slug": "faker",
                  "stats": [
                    {
                      "averages": {
                        "assists": 6,
                        "cs_at_14": 126.67,
                        "cs_diff_at_14": 11,
                        "deaths": 1.33,
                        "gold_earned": 10644,
                        "gold_percentage": 19.91,
                        "gold_spent": 9366.67,
                        "kill_counters": {
                          "inhibitors": 0.33,
                          "neutral_minions": 9,
                          "neutral_minions_enemy_jungle": null,
                          "neutral_minions_team_jungle": null,
                          "players": 4.33,
                          "turrets": 1,
                          "wards": 5.67
                        },
                        "kills": 4.33,
                        "magic_damage": {
                          "dealt": 73223.67,
                          "dealt_percentage": 46.95,
                          "dealt_to_champions": 10190,
                          "dealt_to_champions_percentage": 54.67,
                          "taken": 4951
                        },
                        "minions_killed": 190.67,
                        "physical_damage": {
                          "dealt": 15998.67,
                          "dealt_percentage": 4.7,
                          "dealt_to_champions": 1530,
                          "dealt_to_champions_percentage": 4.85,
                          "taken": 6288.33
                        },
                        "total_damage": {
                          "dealt": 100411.67,
                          "dealt_percentage": 18.06,
                          "dealt_to_champions": 13163.33,
                          "dealt_to_champions_percentage": 22.04,
                          "taken": 11715
                        },
                        "total_heal": 2803.33,
                        "total_time_crowd_control_dealt": 103.33,
                        "total_units_healed": 1,
                        "true_damage": {
                          "dealt": 11189,
                          "dealt_percentage": 18.67,
                          "dealt_to_champions": 1442.33,
                          "dealt_to_champions_percentage": 25.74,
                          "taken": 475
                        },
                        "vision_wards_bought_in_game": 4.67,
                        "wards_placed": 16.33
                      },
                      "games_count": 3,
                      "serie": {
                        "begin_at": "2022-05-09T22:00:00Z",
                        "end_at": "2022-05-29T12:26:00Z",
                        "full_name": "2022",
                        "id": 4534,
                        "league": {
                          "id": 300,
                          "image_url": "https://cdn.pandascore.co/images/league/image/300/900px-msi_2021_lightmode-png",
                          "modified_at": "2019-06-13T11:53:14Z",
                          "name": "Mid-Season Invitational",
                          "slug": "league-of-legends-mid-invitational",
                          "url": null
                        },
                        "league_id": 300,
                        "modified_at": "2022-05-29T17:10:35Z",
                        "name": null,
                        "season": null,
                        "slug": "league-of-legends-mid-invitational-2022",
                        "tournaments": [
                          {
                            "begin_at": "2022-05-09T22:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-05-15T11:00:00Z",
                            "has_bracket": false,
                            "id": 7998,
                            "league_id": 300,
                            "live_supported": true,
                            "modified_at": "2022-05-29T17:10:35Z",
                            "name": "Group A",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4534,
                            "slug": "league-of-legends-mid-invitational-2022-group-a",
                            "tier": "s",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-05-09T22:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-05-14T14:30:00Z",
                            "has_bracket": false,
                            "id": 7999,
                            "league_id": 300,
                            "live_supported": true,
                            "modified_at": "2022-05-29T17:10:35Z",
                            "name": "Group B",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4534,
                            "slug": "league-of-legends-mid-invitational-2022-group-b",
                            "tier": "s",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-05-09T22:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-05-14T11:35:00Z",
                            "has_bracket": false,
                            "id": 8000,
                            "league_id": 300,
                            "live_supported": true,
                            "modified_at": "2022-05-29T17:10:35Z",
                            "name": "Group C",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4534,
                            "slug": "league-of-legends-mid-invitational-2022-group-c",
                            "tier": "s",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-05-19T22:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-05-29T13:00:00Z",
                            "has_bracket": false,
                            "id": 8001,
                            "league_id": 300,
                            "live_supported": true,
                            "modified_at": "2022-05-29T17:10:35Z",
                            "name": "Rumble Stage",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4534,
                            "slug": "league-of-legends-mid-invitational-2022-rumble-stage",
                            "tier": "s",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-05-26T22:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-05-29T12:26:00Z",
                            "has_bracket": true,
                            "id": 8002,
                            "league_id": 300,
                            "live_supported": true,
                            "modified_at": "2023-04-25T16:23:17Z",
                            "name": "Knockout Stage",
                            "prizepool": "250000 United States Dollar",
                            "region": null,
                            "serie_id": 4534,
                            "slug": "league-of-legends-mid-invitational-2022-knockout-stage",
                            "tier": "s",
                            "type": null,
                            "winner_id": 74,
                            "winner_type": "Team"
                          }
                        ],
                        "videogame": {
                          "id": 1,
                          "name": "LoL",
                          "slug": "league-of-legends"
                        },
                        "videogame_title": null,
                        "winner_id": 74,
                        "winner_type": "Team",
                        "year": 2022
                      },
                      "totals": {
                        "assists": 18,
                        "deaths": 4,
                        "games_lost": 0,
                        "games_played": 3,
                        "games_won": 3,
                        "kill_counters": {
                          "inhibitors": 1,
                          "turrets": 3,
                          "wards": 17
                        },
                        "kills": 13,
                        "kills_series": {
                          "double_kills": 1,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 0
                        },
                        "matches_lost": 0,
                        "matches_played": 3,
                        "matches_won": 3,
                        "wards_placed": 49
                      }
                    },
                    {
                      "averages": {
                        "assists": 5.64,
                        "cs_at_14": 131.28,
                        "cs_diff_at_14": -2.76,
                        "deaths": 1.44,
                        "gold_earned": 12372.92,
                        "gold_percentage": 20.63,
                        "gold_spent": 11117.8,
                        "kill_counters": {
                          "inhibitors": 0.16,
                          "neutral_minions": 18.72,
                          "neutral_minions_enemy_jungle": null,
                          "neutral_minions_team_jungle": null,
                          "players": 3.36,
                          "turrets": 1.32,
                          "wards": 8.84
                        },
                        "kills": 3.36,
                        "magic_damage": {
                          "dealt": 117171.16,
                          "dealt_percentage": 54.54,
                          "dealt_to_champions": 12845.32,
                          "dealt_to_champions_percentage": 51.63,
                          "taken": 5522.88
                        },
                        "minions_killed": 254.76,
                        "physical_damage": {
                          "dealt": 26536.16,
                          "dealt_percentage": 5.44,
                          "dealt_to_champions": 1507.88,
                          "dealt_to_champions_percentage": 3.81,
                          "taken": 7535.4
                        },
                        "total_damage": {
                          "dealt": 159175.12,
                          "dealt_percentage": 21,
                          "dealt_to_champions": 15353.76,
                          "dealt_to_champions_percentage": 22.6,
                          "taken": 13677.48
                        },
                        "total_heal": 3834.52,
                        "total_time_crowd_control_dealt": 174.32,
                        "total_units_healed": 1.04,
                        "true_damage": {
                          "dealt": 15467.04,
                          "dealt_percentage": 27.88,
                          "dealt_to_champions": 999.76,
                          "dealt_to_champions_percentage": 21.56,
                          "taken": 618.44
                        },
                        "vision_wards_bought_in_game": 5.84,
                        "wards_placed": 18.56
                      },
                      "games_count": 25,
                      "serie": {
                        "begin_at": "2022-01-12T08:00:00Z",
                        "end_at": "2022-04-02T12:24:00Z",
                        "full_name": "Spring 2022",
                        "id": 4250,
                        "league": {
                          "id": 293,
                          "image_url": "https://cdn.pandascore.co/images/league/image/293/lck_2021_logo-png",
                          "modified_at": "2021-01-06T15:41:48Z",
                          "name": "LCK",
                          "slug": "league-of-legends-lck-champions-korea",
                          "url": null
                        },
                        "league_id": 293,
                        "modified_at": "2022-04-02T13:58:05Z",
                        "name": null,
                        "season": "Spring",
                        "slug": "league-of-legends-lck-champions-korea-spring-2022",
                        "tournaments": [
                          {
                            "begin_at": "2022-01-12T08:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-03-20T12:20:00Z",
                            "has_bracket": false,
                            "id": 7313,
                            "league_id": 293,
                            "live_supported": true,
                            "modified_at": "2022-08-08T14:39:01Z",
                            "name": "Regular Season",
                            "prizepool": null,
                            "region": null,
                            "serie_id": 4250,
                            "slug": "league-of-legends-lck-champions-korea-spring-2022-regular-season",
                            "tier": "a",
                            "type": null,
                            "winner_id": null,
                            "winner_type": "Team"
                          },
                          {
                            "begin_at": "2022-03-23T08:00:00Z",
                            "country": null,
                            "detailed_stats": true,
                            "end_at": "2022-04-02T12:24:00Z",
                            "has_bracket": true,
                            "id": 7628,
                            "league_id": 293,
                            "live_supported": true,
                            "modified_at": "2023-04-25T16:35:34Z",
                            "name": "Playoffs",
                            "prizepool": "375000000 South Korean Won",
                            "region": null,
                            "serie_id": 4250,
                            "slug": "league-of-legends-lck-champions-korea-spring-2022-playoffs",
                            "tier": "a",
                            "type": null,
                            "winner_id": 126061,
                            "winner_type": "Team"
                          }
                        ],
                        "videogame": {
                          "id": 1,
                          "name": "LoL",
                          "slug": "league-of-legends"
                        },
                        "videogame_title": null,
                        "winner_id": 126061,
                        "winner_type": "Team",
                        "year": 2022
                      },
                      "totals": {
                        "assists": 141,
                        "deaths": 36,
                        "games_lost": 3,
                        "games_played": 25,
                        "games_won": 22,
                        "kill_counters": {
                          "inhibitors": 4,
                          "turrets": 33,
                          "wards": 221
                        },
                        "kills": 84,
                        "kills_series": {
                          "double_kills": 8,
                          "penta_kills": 0,
                          "quadra_kills": 0,
                          "triple_kills": 1
                        },
                        "matches_lost": 0,
                        "matches_played": 10,
                        "matches_won": 10,
                        "wards_placed": 464
                      }
                    }
                  ],
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
                  ],
                  "total_stats": {
                    "averages": {
                      "assists": 5.68,
                      "cs_at_14": 130.79,
                      "cs_diff_at_14": -1.29,
                      "deaths": 1.43,
                      "gold_earned": 12187.68,
                      "gold_percentage": 20.28,
                      "gold_spent": 10930.18,
                      "kill_counters": {
                        "inhibitors": 0.18,
                        "neutral_minions": 17.68,
                        "neutral_minions_enemy_jungle": null,
                        "neutral_minions_team_jungle": null,
                        "players": 3.46,
                        "turrets": 1.29,
                        "wards": 8.5
                      },
                      "kills": 3.46,
                      "magic_damage": {
                        "dealt": 112462.5,
                        "dealt_percentage": 53.73,
                        "dealt_to_champions": 12560.82,
                        "dealt_to_champions_percentage": 51.96,
                        "taken": 5461.61
                      },
                      "minions_killed": 247.89,
                      "physical_damage": {
                        "dealt": 25407.14,
                        "dealt_percentage": 5.36,
                        "dealt_to_champions": 1510.25,
                        "dealt_to_champions_percentage": 3.92,
                        "taken": 7401.79
                      },
                      "total_damage": {
                        "dealt": 152879.04,
                        "dealt_percentage": 20.68,
                        "dealt_to_champions": 15119.07,
                        "dealt_to_champions_percentage": 22.54,
                        "taken": 13467.21
                      },
                      "total_heal": 3724.04,
                      "total_time_crowd_control_dealt": 166.71,
                      "total_units_healed": 1.04,
                      "true_damage": {
                        "dealt": 15008.68,
                        "dealt_percentage": 26.89,
                        "dealt_to_champions": 1047.18,
                        "dealt_to_champions_percentage": 22.01,
                        "taken": 603.07
                      },
                      "vision_wards_bought_in_game": 5.71,
                      "wards_placed": 18.32
                    },
                    "games_count": 28,
                    "totals": {
                      "assists": 159,
                      "deaths": 40,
                      "games_lost": 3,
                      "games_played": 28,
                      "games_won": 25,
                      "kill_counters": {
                        "inhibitors": 5,
                        "turrets": 36,
                        "wards": 238
                      },
                      "kills": 97,
                      "kills_series": {
                        "double_kills": 9,
                        "penta_kills": 0,
                        "quadra_kills": 0,
                        "triple_kills": 1
                      },
                      "matches_lost": 0,
                      "matches_played": 13,
                      "matches_won": 13,
                      "wards_placed": 513
                    }
                  }
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLStatsForPlayer"
            }
          }
        },
        "description": "Statistics of a League-of-Legends player\n\nDeprecated fields:\n- last_games[].minions_killed\n"
      }
    },
    "schemas": {
      "LoLStatsForPlayer": {
        "additionalProperties": false,
        "deprecated": false,
        "description": "Aggregated statistics for a player grouped by serie",
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
            "items": {
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
            "title": "LoLPlayerBySerieStats",
            "type": "array"
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
          },
          "total_stats": {
            "additionalProperties": false,
            "deprecated": false,
            "description": "Total Player's statistics",
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
              "totals"
            ],
            "title": "LoLTotalPlayerStat",
            "type": "object"
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
          "teams",
          "total_stats"
        ],
        "title": "LoLStatsForPlayer",
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
    "/lol/players/{player_id_or_slug}/stats": {
      "get": {
        "description": "Get detailed statistics of a given League-of-Legends player\n> ℹ️  \n> \n> This endpoint is only available to customers with a historical or real-time data plan",
        "operationId": "get_lol_players_playerIdOrSlug_stats",
        "parameters": [
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
            "$ref": "#/components/responses/LoLStatsForPlayer"
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
        "summary": "Get stats for LoL player",
        "tags": [
          "LoL stats"
        ],
        "x-pandascore-plan": "Historical plan",
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/players/{player_id_or_slug}/stats' \\\n     --header 'accept: application/json'\n",
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