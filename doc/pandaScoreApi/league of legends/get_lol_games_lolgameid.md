> ## Documentation Index
> Fetch the complete documentation index at: https://developers.pandascore.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a game

Get a single League of Legends game by ID
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
      "LoLGame": {
        "content": {
          "application/json": {
            "examples": {
              "With detailed stats": {
                "description": "/lol/games/243129",
                "value": {
                  "begin_at": "2023-02-20T17:04:44Z",
                  "complete": true,
                  "detailed_stats": true,
                  "end_at": "2023-02-20T17:40:53Z",
                  "finished": true,
                  "forfeit": false,
                  "id": 243129,
                  "length": 1730,
                  "match": {
                    "begin_at": "2023-02-20T17:04:44Z",
                    "detailed_stats": true,
                    "draw": false,
                    "end_at": "2023-02-20T20:34:14Z",
                    "forfeit": false,
                    "game_advantage": null,
                    "games": [
                      {
                        "begin_at": "2023-02-20T17:04:44Z",
                        "complete": true,
                        "detailed_stats": true,
                        "end_at": "2023-02-20T17:40:53Z",
                        "finished": true,
                        "forfeit": false,
                        "id": 243129,
                        "length": 1730,
                        "match_id": 720982,
                        "position": 1,
                        "status": "finished",
                        "winner": {
                          "id": 88,
                          "type": "Team"
                        },
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2023-02-20T17:58:25Z",
                        "complete": true,
                        "detailed_stats": true,
                        "end_at": "2023-02-20T18:28:49Z",
                        "finished": true,
                        "forfeit": false,
                        "id": 243130,
                        "length": 1404,
                        "match_id": 720982,
                        "position": 2,
                        "status": "finished",
                        "winner": {
                          "id": 88,
                          "type": "Team"
                        },
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2023-02-20T18:45:56Z",
                        "complete": true,
                        "detailed_stats": true,
                        "end_at": "2023-02-20T19:19:27Z",
                        "finished": true,
                        "forfeit": false,
                        "id": 243131,
                        "length": 1589,
                        "match_id": 720982,
                        "position": 3,
                        "status": "finished",
                        "winner": {
                          "id": 129970,
                          "type": "Team"
                        },
                        "winner_type": "Team"
                      },
                      {
                        "begin_at": "2023-02-20T19:35:36Z",
                        "complete": true,
                        "detailed_stats": true,
                        "end_at": "2023-02-20T20:34:14Z",
                        "finished": true,
                        "forfeit": false,
                        "id": 243132,
                        "length": 2337,
                        "match_id": 720982,
                        "position": 4,
                        "status": "finished",
                        "winner": {
                          "id": 88,
                          "type": "Team"
                        },
                        "winner_type": "Team"
                      }
                    ],
                    "id": 720982,
                    "league": {
                      "id": 4197,
                      "image_url": "https://cdn-api.pandascore.co/images/league/image/4197/lec_2023-png",
                      "modified_at": "2019-03-03T01:22:54Z",
                      "name": "LEC",
                      "slug": "league-of-legends-lec",
                      "url": null
                    },
                    "league_id": 4197,
                    "live": {
                      "opens_at": "2023-02-20T16:49:44.000000Z",
                      "supported": true,
                      "url": "wss://live.pandascore.co/matches/720982"
                    },
                    "match_type": "best_of",
                    "modified_at": "2023-02-20T20:42:40Z",
                    "name": "Round 1 match 1: KOI vs G2",
                    "number_of_games": 5,
                    "opponents": [
                      {
                        "opponent": {
                          "acronym": "KOI",
                          "dark_mode_image_url": null,
                          "id": 129970,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                          "location": "ES",
                          "modified_at": "2024-12-12T17:14:31Z",
                          "name": "KOI",
                          "slug": "ibai-x-pique"
                        },
                        "type": "Team"
                      },
                      {
                        "opponent": {
                          "acronym": "G2",
                          "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                          "id": 88,
                          "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                          "location": "DE",
                          "modified_at": "2026-03-08T14:48:40Z",
                          "name": "G2 Esports",
                          "slug": "g2-esports"
                        },
                        "type": "Team"
                      }
                    ],
                    "original_scheduled_at": "2023-02-20T17:00:00Z",
                    "rescheduled": false,
                    "results": [
                      {
                        "score": 1,
                        "team_id": 129970
                      },
                      {
                        "score": 3,
                        "team_id": 88
                      }
                    ],
                    "scheduled_at": "2023-02-20T17:00:00Z",
                    "serie": {
                      "begin_at": "2023-01-21T17:00:00Z",
                      "end_at": "2023-02-26T19:41:00Z",
                      "full_name": "Winter 2023",
                      "id": 5386,
                      "league_id": 4197,
                      "modified_at": "2023-02-26T20:27:37Z",
                      "name": "",
                      "season": "Winter",
                      "slug": "league-of-legends-lec-winter-2023",
                      "winner_id": 88,
                      "winner_type": "Team",
                      "year": 2023
                    },
                    "serie_id": 5386,
                    "slug": "2023-02-20-69721ab6-0ff8-4335-87c3-9601afc8a657",
                    "status": "finished",
                    "streams_list": [
                      {
                        "embed_url": "https://player.twitch.tv/?channel=inygontv1",
                        "language": "pt",
                        "main": false,
                        "official": false,
                        "raw_url": "https://www.twitch.tv/inygontv1"
                      },
                      {
                        "embed_url": "https://player.twitch.tv/?channel=lvpes",
                        "language": "es",
                        "main": false,
                        "official": false,
                        "raw_url": "https://www.twitch.tv/lvpes"
                      },
                      {
                        "embed_url": "https://player.twitch.tv/?channel=otplol_",
                        "language": "fr",
                        "main": false,
                        "official": false,
                        "raw_url": "https://www.twitch.tv/otplol_"
                      },
                      {
                        "embed_url": "https://player.twitch.tv/?channel=lec",
                        "language": "en",
                        "main": true,
                        "official": true,
                        "raw_url": "https://www.twitch.tv/lec"
                      }
                    ],
                    "tournament": {
                      "begin_at": "2023-02-20T17:00:00Z",
                      "country": null,
                      "detailed_stats": true,
                      "end_at": "2023-02-26T19:41:00Z",
                      "has_bracket": true,
                      "id": 9913,
                      "league_id": 4197,
                      "live_supported": true,
                      "modified_at": "2023-02-26T20:27:37Z",
                      "name": "Playoffs",
                      "prizepool": null,
                      "region": null,
                      "serie_id": 5386,
                      "slug": "league-of-legends-lec-winter-2023-playoffs",
                      "tier": "a",
                      "type": null,
                      "winner_id": 88,
                      "winner_type": "Team"
                    },
                    "tournament_id": 9913,
                    "videogame": {
                      "id": 1,
                      "name": "LoL",
                      "slug": "league-of-legends"
                    },
                    "videogame_version": {
                      "current": false,
                      "name": "13.1.1"
                    },
                    "winner": {
                      "acronym": "G2",
                      "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                      "id": 88,
                      "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                      "location": "DE",
                      "modified_at": "2026-03-08T14:48:40Z",
                      "name": "G2 Esports",
                      "slug": "g2-esports"
                    },
                    "winner_id": 88,
                    "winner_type": "Team"
                  },
                  "match_id": 720982,
                  "players": [
                    {
                      "assists": 11,
                      "champion": {
                        "id": 3221,
                        "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/1a8ce808-5257-4da7-88ff-4077f96ddc7e.png",
                        "name": "Nautilus",
                        "slug": "Nautilus"
                      },
                      "creep_score": 38,
                      "cs_at_14": 19,
                      "cs_diff_at_14": 17,
                      "deaths": 2,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 243129,
                      "gold_earned": 7119,
                      "gold_percentage": 12.52,
                      "gold_spent": 6075,
                      "items": [
                        {
                          "id": 2449,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6db62c8691e2f6f35efb0eff6e55df41.png",
                          "is_trinket": false,
                          "name": "Ruby Crystal"
                        },
                        {
                          "id": 2449,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6db62c8691e2f6f35efb0eff6e55df41.png",
                          "is_trinket": false,
                          "name": "Ruby Crystal"
                        },
                        {
                          "id": 2537,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                          "is_trinket": false,
                          "name": "Mercury's Treads"
                        },
                        {
                          "id": 2679,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                          "is_trinket": true,
                          "name": "Oracle Lens"
                        },
                        {
                          "id": 2802,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b204c5d1f180ebcba104c5359dbcc05f.png",
                          "is_trinket": false,
                          "name": "Pauldrons of Whiterock"
                        },
                        {
                          "id": 3107,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d59549d4-55e1-4f5b-a1b3-e2799b8b369b.png",
                          "is_trinket": false,
                          "name": "Radiant Virtue"
                        }
                      ],
                      "kills": 0,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 0,
                        "neutral_minions_enemy_jungle": 0,
                        "neutral_minions_team_jungle": 0,
                        "players": 0,
                        "turrets": 0,
                        "wards": 15
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
                      "level": 12,
                      "magic_damage": {
                        "dealt": 7749,
                        "dealt_percentage": 2.43,
                        "dealt_to_champions": 3478,
                        "dealt_to_champions_percentage": 12.7,
                        "taken": 6727
                      },
                      "masteries": [],
                      "minions_killed": 38,
                      "opponent": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "physical_damage": {
                        "dealt": 6445,
                        "dealt_percentage": 1.66,
                        "dealt_to_champions": 1690,
                        "dealt_to_champions_percentage": 3.98,
                        "taken": 12148
                      },
                      "player": {
                        "active": true,
                        "age": 27,
                        "birthday": "1998-11-02",
                        "first_name": "Mihael",
                        "id": 605,
                        "image_url": "https://cdn-api.pandascore.co/images/player/image/605/fnc_mikyx_2025_split_3.png",
                        "last_name": "Mehle",
                        "modified_at": "2025-12-20T08:05:07Z",
                        "name": "Mikyx",
                        "nationality": "SI",
                        "role": "sup",
                        "slug": "mikyx"
                      },
                      "player_id": 605,
                      "role": "sup",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 2,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                          "keystone": {
                            "id": 15,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/61863fdbadbcf32f8274dddf8065c912.png",
                            "name": "Glacial Augment",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 18,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/09d2bb0b95d08979f13568a57be5cc06.png",
                              "name": "Hextech Flashtraption",
                              "type": "slot1"
                            },
                            {
                              "id": 23,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                              "name": "Biscuit Delivery",
                              "type": "slot2"
                            },
                            {
                              "id": 24,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                              "name": "Cosmic Insight",
                              "type": "slot3"
                            }
                          ],
                          "name": "Inspiration",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 4,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                          "lesser_runes": [
                            {
                              "id": 44,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/2763ad2665464bf7e9ff63ab7669b521.png",
                              "name": "Font of Life",
                              "type": "slot1"
                            },
                            {
                              "id": 48,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6054dc49089750c7d576b8e157228f29.png",
                              "name": "Bone Plating",
                              "type": "slot2"
                            }
                          ],
                          "name": "Resolve",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 67,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                            "name": "Armor",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 68,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                            "name": "Magic Resist",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 69,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                            "name": "Attack Speed",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 26,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/fc6bf1688506336009ccf19c4955aa18.png",
                          "name": "Ignite"
                        },
                        {
                          "id": 28,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        }
                      ],
                      "team": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "total_damage": {
                        "dealt": 20075,
                        "dealt_percentage": 2.62,
                        "dealt_to_champions": 5838,
                        "dealt_to_champions_percentage": 7.94,
                        "taken": 19480
                      },
                      "total_heal": 5079,
                      "total_time_crowd_control_dealt": 272,
                      "total_units_healed": 5,
                      "true_damage": {
                        "dealt": 5881,
                        "dealt_percentage": 9.94,
                        "dealt_to_champions": 670,
                        "dealt_to_champions_percentage": 18.53,
                        "taken": 605
                      },
                      "wards": {
                        "placed": 45,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 9
                      },
                      "wards_placed": 45
                    },
                    {
                      "assists": 5,
                      "champion": {
                        "id": 3219,
                        "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/fc5efb6d-d78d-4f1a-8ca4-b13624ee205a.png",
                        "name": "Miss Fortune",
                        "slug": "MissFortune"
                      },
                      "creep_score": 277,
                      "cs_at_14": 126,
                      "cs_diff_at_14": 5,
                      "deaths": 1,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": true
                      },
                      "game_id": 243129,
                      "gold_earned": 15395,
                      "gold_percentage": 27.08,
                      "gold_spent": 13825,
                      "items": [
                        {
                          "id": 2454,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d1be217640f29b7c6b5edc638d1c47d5.png",
                          "is_trinket": false,
                          "name": "Long Sword"
                        },
                        {
                          "id": 2494,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/fcd28e708879aa54037da3539604b1c4.png",
                          "is_trinket": false,
                          "name": "Infinity Edge"
                        },
                        {
                          "id": 2678,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                          "is_trinket": true,
                          "name": "Farsight Alteration"
                        },
                        {
                          "id": 2727,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6c611c3082d7c565a4e4ba63d3255c10.png",
                          "is_trinket": false,
                          "name": "Galeforce"
                        },
                        {
                          "id": 2790,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a900946a4d19c740a092b344807dcb7e.png",
                          "is_trinket": false,
                          "name": "Slightly Magical Footwear"
                        },
                        {
                          "id": 2866,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/9fe203b01a6b9ae1849a8d0d65d4b48b.png",
                          "is_trinket": false,
                          "name": "Bloodthirster"
                        },
                        {
                          "id": 3090,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1cf26db8-7b2a-40cd-b1d4-a256ff0ad801.png",
                          "is_trinket": false,
                          "name": "Lord Dominik's Regards"
                        }
                      ],
                      "kills": 10,
                      "kills_counters": {
                        "inhibitors": 1,
                        "neutral_minions": 16,
                        "neutral_minions_enemy_jungle": 0,
                        "neutral_minions_team_jungle": 12,
                        "players": 10,
                        "turrets": 4,
                        "wards": 10
                      },
                      "kills_series": {
                        "double_kills": 2,
                        "penta_kills": 0,
                        "quadra_kills": 0,
                        "triple_kills": 0
                      },
                      "largest_critical_strike": 1025,
                      "largest_killing_spree": 10,
                      "largest_multi_kill": 2,
                      "level": 15,
                      "magic_damage": {
                        "dealt": 2129,
                        "dealt_percentage": 0.67,
                        "dealt_to_champions": 1447,
                        "dealt_to_champions_percentage": 5.28,
                        "taken": 3064
                      },
                      "masteries": [],
                      "minions_killed": 277,
                      "opponent": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "physical_damage": {
                        "dealt": 209970,
                        "dealt_percentage": 54.13,
                        "dealt_to_champions": 24861,
                        "dealt_to_champions_percentage": 58.51,
                        "taken": 5834
                      },
                      "player": {
                        "active": true,
                        "age": 26,
                        "birthday": "1999-09-02",
                        "first_name": "Steven",
                        "id": 871,
                        "image_url": "https://cdn-api.pandascore.co/images/player/image/871/g2_hans_sama_2025_split_3.png",
                        "last_name": "Liv",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "Hans sama",
                        "nationality": "FR",
                        "role": "adc",
                        "slug": "hans-sama"
                      },
                      "player_id": 871,
                      "role": "adc",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 3,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                          "keystone": {
                            "id": 27,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/2dc7e7cb1ff2b87733d0ca310576819d.png",
                            "name": "Press the Attack",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 33,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                              "name": "Presence of Mind",
                              "type": "slot1"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/078fa7db48ed5384e9933f535f0b986a.png",
                              "name": "Legend: Bloodline",
                              "type": "slot2"
                            },
                            {
                              "id": 38,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/08f4edce2a6f85edbfea701c04314cb9.png",
                              "name": "Cut Down",
                              "type": "slot3"
                            }
                          ],
                          "name": "Precision",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 2,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                          "lesser_runes": [
                            {
                              "id": 19,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                              "name": "Magical Footwear",
                              "type": "slot1"
                            },
                            {
                              "id": 23,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                              "name": "Biscuit Delivery",
                              "type": "slot2"
                            }
                          ],
                          "name": "Inspiration",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 67,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                            "name": "Armor",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 69,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                            "name": "Attack Speed",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 27,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/37e058ce96cf92adf6831ad5946956f4.png",
                          "name": "Exhaust"
                        },
                        {
                          "id": 28,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        }
                      ],
                      "team": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "total_damage": {
                        "dealt": 218372,
                        "dealt_percentage": 28.53,
                        "dealt_to_champions": 26542,
                        "dealt_to_champions_percentage": 36.12,
                        "taken": 9023
                      },
                      "total_heal": 398,
                      "total_time_crowd_control_dealt": 115,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 6272,
                        "dealt_percentage": 10.61,
                        "dealt_to_champions": 234,
                        "dealt_to_champions_percentage": 6.47,
                        "taken": 123
                      },
                      "wards": {
                        "placed": 12,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 4
                      },
                      "wards_placed": 12
                    },
                    {
                      "assists": 5,
                      "champion": {
                        "id": 3247,
                        "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/90bfe6b6-2dd8-4dfc-b1df-769cbf6ab088.png",
                        "name": "Jayce",
                        "slug": "Jayce"
                      },
                      "creep_score": 238,
                      "cs_at_14": 100,
                      "cs_diff_at_14": -12,
                      "deaths": 4,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": true,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 243129,
                      "gold_earned": 12404,
                      "gold_percentage": 21.82,
                      "gold_spent": 9775,
                      "items": [
                        {
                          "id": 2454,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d1be217640f29b7c6b5edc638d1c47d5.png",
                          "is_trinket": false,
                          "name": "Long Sword"
                        },
                        {
                          "id": 2537,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                          "is_trinket": false,
                          "name": "Mercury's Treads"
                        },
                        {
                          "id": 2679,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                          "is_trinket": true,
                          "name": "Oracle Lens"
                        },
                        {
                          "id": 3059,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/8bbd4abd-2658-4841-9b57-28acbdced753.png",
                          "is_trinket": false,
                          "name": "Eclipse"
                        },
                        {
                          "id": 3070,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a5144a5e-4ba3-4400-bca8-6fbccc59e324.png",
                          "is_trinket": false,
                          "name": "Last Whisper"
                        },
                        {
                          "id": 3071,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/325fc643-cc72-4b69-9ce9-7bbd931a60f5.png",
                          "is_trinket": false,
                          "name": "Muramana"
                        }
                      ],
                      "kills": 5,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 17,
                        "neutral_minions_enemy_jungle": 5,
                        "neutral_minions_team_jungle": 9,
                        "players": 5,
                        "turrets": 4,
                        "wards": 12
                      },
                      "kills_series": {
                        "double_kills": 2,
                        "penta_kills": 0,
                        "quadra_kills": 0,
                        "triple_kills": 0
                      },
                      "largest_critical_strike": 0,
                      "largest_killing_spree": 5,
                      "largest_multi_kill": 2,
                      "level": 16,
                      "magic_damage": {
                        "dealt": 12532,
                        "dealt_percentage": 3.94,
                        "dealt_to_champions": 1847,
                        "dealt_to_champions_percentage": 6.75,
                        "taken": 9562
                      },
                      "masteries": [],
                      "minions_killed": 238,
                      "opponent": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "physical_damage": {
                        "dealt": 135358,
                        "dealt_percentage": 34.9,
                        "dealt_to_champions": 15381,
                        "dealt_to_champions_percentage": 36.2,
                        "taken": 10393
                      },
                      "player": {
                        "active": true,
                        "age": 26,
                        "birthday": "1999-11-17",
                        "first_name": "Rasmus",
                        "id": 1132,
                        "image_url": "https://cdn-api.pandascore.co/images/player/image/1132/g2_caps_2025_split_3.png",
                        "last_name": "Winther",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "Caps",
                        "nationality": "DK",
                        "role": "mid",
                        "slug": "caps"
                      },
                      "player_id": 1132,
                      "role": "mid",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 1,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                          "keystone": {
                            "id": 1,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/617036006e61b2b07fb3da33f634dad7.png",
                            "name": "Electrocute",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 6,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/faae66d46ae5bc177a56890342087ac2.png",
                              "name": "Taste of Blood",
                              "type": "slot1"
                            },
                            {
                              "id": 8,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a5317349f8ce3e0923fe970e5232bf30.png",
                              "name": "Zombie Ward",
                              "type": "slot2"
                            },
                            {
                              "id": 11,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/569a1e7d3c46d9731392616eccebdd9c.png",
                              "name": "Treasure Hunter",
                              "type": "slot3"
                            }
                          ],
                          "name": "Domination",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 4,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                          "lesser_runes": [
                            {
                              "id": 47,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                              "name": "Second Wind",
                              "type": "slot2"
                            },
                            {
                              "id": 49,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/96f9d32b50d28f0d76f7db0eb310841d.png",
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
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                            "name": "Magic Resist",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 39,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                          "name": "Teleport"
                        }
                      ],
                      "team": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "total_damage": {
                        "dealt": 147890,
                        "dealt_percentage": 19.32,
                        "dealt_to_champions": 17229,
                        "dealt_to_champions_percentage": 23.44,
                        "taken": 20217
                      },
                      "total_heal": 4214,
                      "total_time_crowd_control_dealt": 69,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 0,
                        "dealt_percentage": 0,
                        "dealt_to_champions": 0,
                        "dealt_to_champions_percentage": 0,
                        "taken": 261
                      },
                      "wards": {
                        "placed": 18,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 3
                      },
                      "wards_placed": 18
                    },
                    {
                      "assists": 3,
                      "champion": {
                        "id": 3121,
                        "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/1a602e7dc475be3ca9ccba41689c71d3.png",
                        "name": "Viktor",
                        "slug": "Viktor"
                      },
                      "creep_score": 229,
                      "cs_at_14": 112,
                      "cs_diff_at_14": 12,
                      "deaths": 4,
                      "flags": {
                        "first_blood_assist": true,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 243129,
                      "gold_earned": 10048,
                      "gold_percentage": 21.59,
                      "gold_spent": 10075,
                      "items": [
                        {
                          "id": 2447,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/93bb71d5aba94a73ab32a16bf3708869.png",
                          "is_trinket": false,
                          "name": "Blasting Wand"
                        },
                        {
                          "id": 2473,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/7e869611bdd37522a83fb50079aadafb.png",
                          "is_trinket": false,
                          "name": "Corrupting Potion"
                        },
                        {
                          "id": 2677,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d764e2dad4b185bbbbc86ca2998d5313.png",
                          "is_trinket": true,
                          "name": "Stealth Ward"
                        },
                        {
                          "id": 2814,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/f40c1900cda35abdb97fe82172530b79.png",
                          "is_trinket": false,
                          "name": "Rabadon's Deathcap"
                        },
                        {
                          "id": 2832,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                          "is_trinket": false,
                          "name": "Ionian Boots of Lucidity"
                        },
                        {
                          "id": 3043,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3c9dee81-cfff-4920-87ad-e0516ac0fc92.png",
                          "is_trinket": false,
                          "name": "Stopwatch"
                        },
                        {
                          "id": 3128,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a51f01be-6962-4d52-9ea1-98290f2e4fdd.png",
                          "is_trinket": false,
                          "name": "Rod of Ages"
                        }
                      ],
                      "kills": 2,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 0,
                        "neutral_minions_enemy_jungle": 0,
                        "neutral_minions_team_jungle": 0,
                        "players": 2,
                        "turrets": 1,
                        "wards": 3
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
                      "level": 15,
                      "magic_damage": {
                        "dealt": 121911,
                        "dealt_percentage": 66.47,
                        "dealt_to_champions": 13239,
                        "dealt_to_champions_percentage": 49.89,
                        "taken": 4795
                      },
                      "masteries": [],
                      "minions_killed": 229,
                      "opponent": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "physical_damage": {
                        "dealt": 10317,
                        "dealt_percentage": 2.92,
                        "dealt_to_champions": 932,
                        "dealt_to_champions_percentage": 3.13,
                        "taken": 13173
                      },
                      "player": {
                        "active": true,
                        "age": 25,
                        "birthday": "2000-03-30",
                        "first_name": "Emil",
                        "id": 1429,
                        "image_url": "https://cdn-api.pandascore.co/images/player/image/1429/rge_larssen_2024_split_1.png",
                        "last_name": "Larsson",
                        "modified_at": "2025-07-29T07:48:15Z",
                        "name": "Larssen",
                        "nationality": "SE",
                        "role": "mid",
                        "slug": "larssen"
                      },
                      "player_id": 1429,
                      "role": "mid",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 5,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                          "keystone": {
                            "id": 52,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fbe3405d6a68d3b7ae3f305fdf129e99.png",
                            "name": "Summon Aery",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 56,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                              "name": "Manaflow Band",
                              "type": "slot1"
                            },
                            {
                              "id": 58,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/632a47c2a88802029838e383a866feb1.png",
                              "name": "Transcendence",
                              "type": "slot2"
                            },
                            {
                              "id": 61,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                              "name": "Scorch",
                              "type": "slot3"
                            }
                          ],
                          "name": "Sorcery",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 1,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                          "lesser_runes": [
                            {
                              "id": 6,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/faae66d46ae5bc177a56890342087ac2.png",
                              "name": "Taste of Blood",
                              "type": "slot1"
                            },
                            {
                              "id": 9,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/9406d2cb2aa41a5d61aed593e2ba75cc.png",
                              "name": "Ghost Poro",
                              "type": "slot2"
                            }
                          ],
                          "name": "Domination",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 67,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                            "name": "Armor",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 69,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                            "name": "Attack Speed",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 39,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                          "name": "Teleport"
                        }
                      ],
                      "team": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "total_damage": {
                        "dealt": 132228,
                        "dealt_percentage": 22.56,
                        "dealt_to_champions": 14171,
                        "dealt_to_champions_percentage": 24.56,
                        "taken": 18371
                      },
                      "total_heal": 2344,
                      "total_time_crowd_control_dealt": 208,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 0,
                        "dealt_percentage": 0,
                        "dealt_to_champions": 0,
                        "dealt_to_champions_percentage": 0,
                        "taken": 402
                      },
                      "wards": {
                        "placed": 12,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 3
                      },
                      "wards_placed": 12
                    },
                    {
                      "assists": 5,
                      "champion": {
                        "id": 3016,
                        "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/e7eb3fb357e71d7673434cef9ca1ffe2.png",
                        "name": "Gragas",
                        "slug": "Gragas"
                      },
                      "creep_score": 254,
                      "cs_at_14": 121,
                      "cs_diff_at_14": -25,
                      "deaths": 0,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 243129,
                      "gold_earned": 10565,
                      "gold_percentage": 18.58,
                      "gold_spent": 8885,
                      "items": [
                        {
                          "id": 2460,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/0f07d995a4de9dc12ffaf8c403658755.png",
                          "is_trinket": false,
                          "name": "Amplifying Tome"
                        },
                        {
                          "id": 2678,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                          "is_trinket": true,
                          "name": "Farsight Alteration"
                        },
                        {
                          "id": 2832,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                          "is_trinket": false,
                          "name": "Ionian Boots of Lucidity"
                        },
                        {
                          "id": 2893,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/47c001c40f4d6d169be155b0a74e08d5.png",
                          "is_trinket": false,
                          "name": "Seraph's Embrace"
                        },
                        {
                          "id": 3044,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d0e13016-50c3-4bf8-926c-a502cced78c4.png",
                          "is_trinket": false,
                          "name": "Broken Stopwatch"
                        },
                        {
                          "id": 3128,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a51f01be-6962-4d52-9ea1-98290f2e4fdd.png",
                          "is_trinket": false,
                          "name": "Rod of Ages"
                        }
                      ],
                      "kills": 0,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 4,
                        "neutral_minions_enemy_jungle": 0,
                        "neutral_minions_team_jungle": 3,
                        "players": 0,
                        "turrets": 1,
                        "wards": 3
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
                        "dealt": 147474,
                        "dealt_percentage": 46.33,
                        "dealt_to_champions": 7029,
                        "dealt_to_champions_percentage": 25.67,
                        "taken": 4264
                      },
                      "masteries": [],
                      "minions_killed": 254,
                      "opponent": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "physical_damage": {
                        "dealt": 15775,
                        "dealt_percentage": 4.07,
                        "dealt_to_champions": 252,
                        "dealt_to_champions_percentage": 0.59,
                        "taken": 17621
                      },
                      "player": {
                        "active": true,
                        "age": 26,
                        "birthday": "2000-01-19",
                        "first_name": "Sergen",
                        "id": 1718,
                        "image_url": "https://cdn-api.pandascore.co/images/player/image/1718/g2_broken_blade_2025_split_3.png",
                        "last_name": "Çelik",
                        "modified_at": "2026-03-08T14:48:38Z",
                        "name": "BrokenBlade",
                        "nationality": "DE",
                        "role": "top",
                        "slug": "broken-blade"
                      },
                      "player_id": 1718,
                      "role": "top",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 5,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                          "keystone": {
                            "id": 53,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/b8282c680e5d022dc564c54937a20a26.png",
                            "name": "Arcane Comet",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 56,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                              "name": "Manaflow Band",
                              "type": "slot1"
                            },
                            {
                              "id": 58,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/632a47c2a88802029838e383a866feb1.png",
                              "name": "Transcendence",
                              "type": "slot2"
                            },
                            {
                              "id": 61,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                              "name": "Scorch",
                              "type": "slot3"
                            }
                          ],
                          "name": "Sorcery",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 2,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                          "lesser_runes": [
                            {
                              "id": 23,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                              "name": "Biscuit Delivery",
                              "type": "slot2"
                            },
                            {
                              "id": 24,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                              "name": "Cosmic Insight",
                              "type": "slot3"
                            }
                          ],
                          "name": "Inspiration",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 67,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                            "name": "Armor",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 70,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f847b627-6b53-413f-8b87-939c3dd437bb.png",
                            "name": "Ability Haste",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 39,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                          "name": "Teleport"
                        }
                      ],
                      "team": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "total_damage": {
                        "dealt": 164759,
                        "dealt_percentage": 21.53,
                        "dealt_to_champions": 7282,
                        "dealt_to_champions_percentage": 9.91,
                        "taken": 22004
                      },
                      "total_heal": 13930,
                      "total_time_crowd_control_dealt": 396,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 1510,
                        "dealt_percentage": 2.55,
                        "dealt_to_champions": 0,
                        "dealt_to_champions_percentage": 0,
                        "taken": 118
                      },
                      "wards": {
                        "placed": 15,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 6
                      },
                      "wards_placed": 15
                    },
                    {
                      "assists": 4,
                      "champion": {
                        "id": 3085,
                        "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/334bbb28d99b00df03f7c28e929457ce.png",
                        "name": "Sejuani",
                        "slug": "Sejuani"
                      },
                      "creep_score": 127,
                      "cs_at_14": 57,
                      "cs_diff_at_14": -22,
                      "deaths": 4,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": true,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 243129,
                      "gold_earned": 8470,
                      "gold_percentage": 18.2,
                      "gold_spent": 8175,
                      "items": [
                        {
                          "id": 2504,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/339e734119952a522185cf5bd0729299.png",
                          "is_trinket": false,
                          "name": "Plated Steelcaps"
                        },
                        {
                          "id": 2679,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                          "is_trinket": true,
                          "name": "Oracle Lens"
                        },
                        {
                          "id": 2688,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c38d52b6bb9b984bf353c56585dae43d.png",
                          "is_trinket": false,
                          "name": "Force of Nature"
                        },
                        {
                          "id": 3107,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d59549d4-55e1-4f5b-a1b3-e2799b8b369b.png",
                          "is_trinket": false,
                          "name": "Radiant Virtue"
                        }
                      ],
                      "kills": 1,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 98,
                        "neutral_minions_enemy_jungle": 0,
                        "neutral_minions_team_jungle": 71,
                        "players": 1,
                        "turrets": 0,
                        "wards": 13
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
                      "level": 12,
                      "magic_damage": {
                        "dealt": 24336,
                        "dealt_percentage": 13.27,
                        "dealt_to_champions": 3737,
                        "dealt_to_champions_percentage": 14.08,
                        "taken": 8083
                      },
                      "masteries": [],
                      "minions_killed": 127,
                      "opponent": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "physical_damage": {
                        "dealt": 59981,
                        "dealt_percentage": 16.98,
                        "dealt_to_champions": 3848,
                        "dealt_to_champions_percentage": 12.9,
                        "taken": 12941
                      },
                      "player": {
                        "active": true,
                        "age": 26,
                        "birthday": "2000-02-09",
                        "first_name": "Kim",
                        "id": 2538,
                        "image_url": "https://cdn-api.pandascore.co/images/player/image/2538/navi_malrang_2025_split_3.png",
                        "last_name": "Geun-seong",
                        "modified_at": "2025-12-30T16:22:49Z",
                        "name": "Malrang",
                        "nationality": "KR",
                        "role": "sup",
                        "slug": "malrang"
                      },
                      "player_id": 2538,
                      "role": "jun",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 4,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                          "keystone": {
                            "id": 41,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a8f562990b0c66277ffcf1f1245582ca.png",
                            "name": "Aftershock",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 44,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/2763ad2665464bf7e9ff63ab7669b521.png",
                              "name": "Font of Life",
                              "type": "slot1"
                            },
                            {
                              "id": 48,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/6054dc49089750c7d576b8e157228f29.png",
                              "name": "Bone Plating",
                              "type": "slot2"
                            },
                            {
                              "id": 51,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                              "name": "Unflinching",
                              "type": "slot3"
                            }
                          ],
                          "name": "Resolve",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 1,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                          "lesser_runes": [
                            {
                              "id": 14,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c9305f3dcdc9b6711f90df9e6e0c849c.png",
                              "name": "Ultimate Hunter",
                              "type": "slot3"
                            },
                            {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/eea2c6cd75310f68cce8a704f37cf296.png",
                              "name": "Cheap Shot",
                              "type": "slot1"
                            }
                          ],
                          "name": "Domination",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 67,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                            "name": "Armor",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 69,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                            "name": "Attack Speed",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 36,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                          "name": "Smite"
                        }
                      ],
                      "team": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "total_damage": {
                        "dealt": 117282,
                        "dealt_percentage": 20.01,
                        "dealt_to_champions": 8326,
                        "dealt_to_champions_percentage": 14.43,
                        "taken": 22201
                      },
                      "total_heal": 2347,
                      "total_time_crowd_control_dealt": 271,
                      "total_units_healed": 5,
                      "true_damage": {
                        "dealt": 32963,
                        "dealt_percentage": 66.76,
                        "dealt_to_champions": 740,
                        "dealt_to_champions_percentage": 55.18,
                        "taken": 1176
                      },
                      "wards": {
                        "placed": 11,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 9
                      },
                      "wards_placed": 11
                    },
                    {
                      "assists": 1,
                      "champion": {
                        "id": 3168,
                        "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/763b77b9-90be-4f4c-b8fa-4fc321aedb25.png",
                        "name": "Gnar",
                        "slug": "Gnar"
                      },
                      "creep_score": 289,
                      "cs_at_14": 146,
                      "cs_diff_at_14": 25,
                      "deaths": 2,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 243129,
                      "gold_earned": 11013,
                      "gold_percentage": 23.67,
                      "gold_spent": 10308,
                      "items": [
                        {
                          "id": 2465,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/167abf5d0dc59292a78b79ceadffcc99.png",
                          "is_trinket": false,
                          "name": "Negatron Cloak"
                        },
                        {
                          "id": 2522,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/793611e388bdaddc96e973d535b280d9.png",
                          "is_trinket": false,
                          "name": "Warden's Mail"
                        },
                        {
                          "id": 2537,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/fc3c2be90b25dd98ce8826dfc66e1be7.png",
                          "is_trinket": false,
                          "name": "Mercury's Treads"
                        },
                        {
                          "id": 2678,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                          "is_trinket": true,
                          "name": "Farsight Alteration"
                        },
                        {
                          "id": 2927,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/a3d78560d3945a73d66da14f28d6b759.png",
                          "is_trinket": false,
                          "name": "Black Cleaver"
                        },
                        {
                          "id": 2929,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/5b92dcbb3d964c0ad39b320d55601c9a.png",
                          "is_trinket": false,
                          "name": "Trinity Force"
                        }
                      ],
                      "kills": 1,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 12,
                        "neutral_minions_enemy_jungle": 0,
                        "neutral_minions_team_jungle": 11,
                        "players": 1,
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
                      "largest_killing_spree": 0,
                      "largest_multi_kill": 1,
                      "level": 16,
                      "magic_damage": {
                        "dealt": 17328,
                        "dealt_percentage": 9.45,
                        "dealt_to_champions": 3059,
                        "dealt_to_champions_percentage": 11.53,
                        "taken": 7615
                      },
                      "masteries": [],
                      "minions_killed": 289,
                      "opponent": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "physical_damage": {
                        "dealt": 154103,
                        "dealt_percentage": 43.62,
                        "dealt_to_champions": 14839,
                        "dealt_to_champions_percentage": 49.76,
                        "taken": 13021
                      },
                      "player": {
                        "active": true,
                        "age": 24,
                        "birthday": "2001-04-14",
                        "first_name": "Mathias",
                        "id": 20300,
                        "image_url": "https://cdn-api.pandascore.co/images/player/image/20300/bkr_szygenda_2025_split_2.png",
                        "last_name": "Jensen",
                        "modified_at": "2025-11-05T09:58:17Z",
                        "name": "Szygenda",
                        "nationality": "DK",
                        "role": "top",
                        "slug": "szygenda"
                      },
                      "player_id": 20300,
                      "role": "top",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 3,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                          "keystone": {
                            "id": 29,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d7dee9f79afc995429521e2b586aae87.png",
                            "name": "Fleet Footwork",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 32,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f84c3f1382361720c8acf85febfd7461.png",
                              "name": "Triumph",
                              "type": "slot1"
                            },
                            {
                              "id": 35,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/8e7ad3c9bbb91721bbe8b1fb1e0d1915.png",
                              "name": "Legend: Tenacity",
                              "type": "slot2"
                            },
                            {
                              "id": 39,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/726099ed11eed3e8515e702abd2bbf2a.png",
                              "name": "Last Stand",
                              "type": "slot3"
                            }
                          ],
                          "name": "Precision",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 4,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/54c94cceac3bd8cf21be2a1e537a8880.png",
                          "lesser_runes": [
                            {
                              "id": 47,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/3734b985fdb6c75e91ec7e0b92034869.png",
                              "name": "Second Wind",
                              "type": "slot2"
                            },
                            {
                              "id": 51,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f6d5a0635d6ffa966708963cc4e1afc7.png",
                              "name": "Unflinching",
                              "type": "slot3"
                            }
                          ],
                          "name": "Resolve",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 68,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fcfed701-ffbd-484b-9ba2-f3e7c24772fc.png",
                            "name": "Magic Resist",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 69,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                            "name": "Attack Speed",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 39,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/76f3d1cbc7111379f6efe2d1098b04c4.png",
                          "name": "Teleport"
                        }
                      ],
                      "team": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "total_damage": {
                        "dealt": 175706,
                        "dealt_percentage": 29.98,
                        "dealt_to_champions": 17899,
                        "dealt_to_champions_percentage": 31.02,
                        "taken": 21217
                      },
                      "total_heal": 4734,
                      "total_time_crowd_control_dealt": 457,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 4275,
                        "dealt_percentage": 8.66,
                        "dealt_to_champions": 0,
                        "dealt_to_champions_percentage": 0,
                        "taken": 581
                      },
                      "wards": {
                        "placed": 13,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 3
                      },
                      "wards_placed": 13
                    },
                    {
                      "assists": 3,
                      "champion": {
                        "id": 3215,
                        "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/ad8d5716-9550-4922-8240-bca395b16615.png",
                        "name": "Lucian",
                        "slug": "Lucian"
                      },
                      "creep_score": 248,
                      "cs_at_14": 121,
                      "cs_diff_at_14": -5,
                      "deaths": 4,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 243129,
                      "gold_earned": 10870,
                      "gold_percentage": 23.36,
                      "gold_spent": 10825,
                      "items": [
                        {
                          "id": 2474,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                          "is_trinket": false,
                          "name": "Control Ward"
                        },
                        {
                          "id": 2494,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/fcd28e708879aa54037da3539604b1c4.png",
                          "is_trinket": false,
                          "name": "Infinity Edge"
                        },
                        {
                          "id": 2641,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/ea30f12493c7ead150d4219126965550.png",
                          "is_trinket": false,
                          "name": "Doran's Blade"
                        },
                        {
                          "id": 2678,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/3d5c76c6af5cb6ed66394086f0232500.png",
                          "is_trinket": true,
                          "name": "Farsight Alteration"
                        },
                        {
                          "id": 2714,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/2e9e74676892b4fbaf86c33e959bf373.png",
                          "is_trinket": false,
                          "name": "Rapid Firecannon"
                        },
                        {
                          "id": 2727,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/6c611c3082d7c565a4e4ba63d3255c10.png",
                          "is_trinket": false,
                          "name": "Galeforce"
                        },
                        {
                          "id": 2832,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                          "is_trinket": false,
                          "name": "Ionian Boots of Lucidity"
                        }
                      ],
                      "kills": 2,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 12,
                        "neutral_minions_enemy_jungle": 0,
                        "neutral_minions_team_jungle": 8,
                        "players": 2,
                        "turrets": 0,
                        "wards": 8
                      },
                      "kills_series": {
                        "double_kills": 0,
                        "penta_kills": 0,
                        "quadra_kills": 0,
                        "triple_kills": 0
                      },
                      "largest_critical_strike": 402,
                      "largest_killing_spree": 2,
                      "largest_multi_kill": 1,
                      "level": 13,
                      "magic_damage": {
                        "dealt": 14189,
                        "dealt_percentage": 7.74,
                        "dealt_to_champions": 3202,
                        "dealt_to_champions_percentage": 12.07,
                        "taken": 5114
                      },
                      "masteries": [],
                      "minions_killed": 248,
                      "opponent": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "physical_damage": {
                        "dealt": 125424,
                        "dealt_percentage": 35.5,
                        "dealt_to_champions": 9384,
                        "dealt_to_champions_percentage": 31.47,
                        "taken": 10367
                      },
                      "player": {
                        "active": true,
                        "age": 24,
                        "birthday": "2001-12-20",
                        "first_name": "Markos",
                        "id": 21577,
                        "image_url": "https://cdn-api.pandascore.co/images/player/image/21577/m8_comp_2025_split_2.png",
                        "last_name": "Stamkopoulos",
                        "modified_at": "2026-02-23T14:25:31Z",
                        "name": "Comp",
                        "nationality": "GR",
                        "role": "adc",
                        "slug": "comp"
                      },
                      "player_id": 21577,
                      "role": "adc",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 2,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                          "keystone": {
                            "id": 65,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/13598521aebb0be68b52982d46aa1b1c.png",
                            "name": "First Strike",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 19,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                              "name": "Magical Footwear",
                              "type": "slot1"
                            },
                            {
                              "id": 23,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/1194b748d247fd494e848490df06e439.png",
                              "name": "Biscuit Delivery",
                              "type": "slot2"
                            },
                            {
                              "id": 24,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                              "name": "Cosmic Insight",
                              "type": "slot3"
                            }
                          ],
                          "name": "Inspiration",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 3,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/6aac126e9e7489812bb15e3ff4855f70.png",
                          "lesser_runes": [
                            {
                              "id": 33,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/63f58c2d747e2997472d1a3af2450e4e.png",
                              "name": "Presence of Mind",
                              "type": "slot1"
                            },
                            {
                              "id": 36,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/078fa7db48ed5384e9933f535f0b986a.png",
                              "name": "Legend: Bloodline",
                              "type": "slot2"
                            }
                          ],
                          "name": "Precision",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 67,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                            "name": "Armor",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 69,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/a778cbbb-0ebf-4ef9-8ff2-5b226bbc1e0d.png",
                            "name": "Attack Speed",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 23,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/65eea722a1fc79fb6469e7246eb0afb8.png",
                          "name": "Cleanse"
                        },
                        {
                          "id": 28,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        }
                      ],
                      "team": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "total_damage": {
                        "dealt": 151750,
                        "dealt_percentage": 25.89,
                        "dealt_to_champions": 13188,
                        "dealt_to_champions_percentage": 22.85,
                        "taken": 16305
                      },
                      "total_heal": 1357,
                      "total_time_crowd_control_dealt": 35,
                      "total_units_healed": 1,
                      "true_damage": {
                        "dealt": 12136,
                        "dealt_percentage": 24.58,
                        "dealt_to_champions": 601,
                        "dealt_to_champions_percentage": 44.82,
                        "taken": 824
                      },
                      "wards": {
                        "placed": 11,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 3
                      },
                      "wards_placed": 11
                    },
                    {
                      "assists": 4,
                      "champion": {
                        "id": 3059,
                        "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/e8bad58096e0bf120d2945d2ae8c83cb.png",
                        "name": "Nami",
                        "slug": "Nami"
                      },
                      "creep_score": 9,
                      "cs_at_14": 2,
                      "cs_diff_at_14": -17,
                      "deaths": 4,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 243129,
                      "gold_earned": 6135,
                      "gold_percentage": 13.18,
                      "gold_spent": 6050,
                      "items": [
                        {
                          "id": 2465,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/167abf5d0dc59292a78b79ceadffcc99.png",
                          "is_trinket": false,
                          "name": "Negatron Cloak"
                        },
                        {
                          "id": 2474,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1c52d50042ba9df5493d99cb10668573.png",
                          "is_trinket": false,
                          "name": "Control Ward"
                        },
                        {
                          "id": 2679,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                          "is_trinket": true,
                          "name": "Oracle Lens"
                        },
                        {
                          "id": 2720,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d703d8cf515d6fef18fdbacd320248ad.png",
                          "is_trinket": false,
                          "name": "Imperial Mandate"
                        },
                        {
                          "id": 2800,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/97344af466a4d836bf56a2784867b6d2.png",
                          "is_trinket": false,
                          "name": "Shard of True Ice"
                        },
                        {
                          "id": 2832,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                          "is_trinket": false,
                          "name": "Ionian Boots of Lucidity"
                        },
                        {
                          "id": 3016,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/b4e5bb16fbc4368c43c9712a2a154e6f.png",
                          "is_trinket": false,
                          "name": "Oblivion Orb"
                        }
                      ],
                      "kills": 1,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 0,
                        "neutral_minions_enemy_jungle": 0,
                        "neutral_minions_team_jungle": 0,
                        "players": 1,
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
                      "largest_multi_kill": 1,
                      "level": 11,
                      "magic_damage": {
                        "dealt": 5645,
                        "dealt_percentage": 3.08,
                        "dealt_to_champions": 3302,
                        "dealt_to_champions_percentage": 12.44,
                        "taken": 3796
                      },
                      "masteries": [],
                      "minions_killed": 9,
                      "opponent": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "physical_damage": {
                        "dealt": 3462,
                        "dealt_percentage": 0.98,
                        "dealt_to_champions": 820,
                        "dealt_to_champions_percentage": 2.75,
                        "taken": 8374
                      },
                      "player": {
                        "active": true,
                        "age": 25,
                        "birthday": "2000-10-20",
                        "first_name": "Adrian",
                        "id": 22950,
                        "image_url": "https://cdn-api.pandascore.co/images/player/image/22950/vks_trymbi_2025_split_3.png",
                        "last_name": "Trybus",
                        "modified_at": "2025-12-21T12:19:02Z",
                        "name": "Trymbi",
                        "nationality": "PL",
                        "role": "sup",
                        "slug": "trymbi"
                      },
                      "player_id": 22950,
                      "role": "sup",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 5,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/fedb6f0ca24988f397ad65670e1f9f76.png",
                          "keystone": {
                            "id": 52,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/fbe3405d6a68d3b7ae3f305fdf129e99.png",
                            "name": "Summon Aery",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 56,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/ce8144471d3d5b3ab7b13ceede28480f.png",
                              "name": "Manaflow Band",
                              "type": "slot1"
                            },
                            {
                              "id": 58,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/632a47c2a88802029838e383a866feb1.png",
                              "name": "Transcendence",
                              "type": "slot2"
                            },
                            {
                              "id": 61,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/c34c227ecf5a2cb963ecde2005474d29.png",
                              "name": "Scorch",
                              "type": "slot3"
                            }
                          ],
                          "name": "Sorcery",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 2,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                          "lesser_runes": [
                            {
                              "id": 21,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/032d8f7fe2b24e22e8740bcca4e4d84c.png",
                              "name": "Future's Market",
                              "type": "slot2"
                            },
                            {
                              "id": 19,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                              "name": "Magical Footwear",
                              "type": "slot1"
                            }
                          ],
                          "name": "Inspiration",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 67,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f13b21b9-7181-4e48-ba9c-398f1e87ef8b.png",
                            "name": "Armor",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 30,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/62cc94a564835cd3abd80d74346c35da.png",
                          "name": "Heal"
                        }
                      ],
                      "team": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "total_damage": {
                        "dealt": 9107,
                        "dealt_percentage": 1.55,
                        "dealt_to_champions": 4122,
                        "dealt_to_champions_percentage": 7.14,
                        "taken": 12801
                      },
                      "total_heal": 6406,
                      "total_time_crowd_control_dealt": 137,
                      "total_units_healed": 5,
                      "true_damage": {
                        "dealt": 0,
                        "dealt_percentage": 0,
                        "dealt_to_champions": 0,
                        "dealt_to_champions_percentage": 0,
                        "taken": 629
                      },
                      "wards": {
                        "placed": 31,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 6
                      },
                      "wards_placed": 31
                    },
                    {
                      "assists": 13,
                      "champion": {
                        "id": 3053,
                        "image_url": "https://cdn-api.pandascore.co/images/lol/champion/image/d8cee56dc327f130e470caf9871b2654.png",
                        "name": "Maokai",
                        "slug": "Maokai"
                      },
                      "creep_score": 155,
                      "cs_at_14": 79,
                      "cs_diff_at_14": 22,
                      "deaths": 0,
                      "flags": {
                        "first_blood_assist": false,
                        "first_blood_kill": false,
                        "first_inhibitor_assist": false,
                        "first_inhibitor_kill": false,
                        "first_tower_assist": false,
                        "first_tower_kill": false
                      },
                      "game_id": 243129,
                      "gold_earned": 11367,
                      "gold_percentage": 19.99,
                      "gold_spent": 9300,
                      "items": [
                        {
                          "id": 2445,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/5d76fb8969392486363994c43a0abc2d.png",
                          "is_trinket": false,
                          "name": "Giant's Belt"
                        },
                        {
                          "id": 2512,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/1e29f7f8a099017ed7b1a6333a9357b1.png",
                          "is_trinket": false,
                          "name": "Kindlegem"
                        },
                        {
                          "id": 2679,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/c3206a950b4e5f26ffe6d7faef072f8c.png",
                          "is_trinket": true,
                          "name": "Oracle Lens"
                        },
                        {
                          "id": 2832,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/220e7ad7d76b4903e6af1aa93566a310.png",
                          "is_trinket": false,
                          "name": "Ionian Boots of Lucidity"
                        },
                        {
                          "id": 3066,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/44b9ad9a-377a-49a8-9122-85484ce58c2b.png",
                          "is_trinket": false,
                          "name": "Demonic Embrace"
                        },
                        {
                          "id": 3107,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/item/image/d59549d4-55e1-4f5b-a1b3-e2799b8b369b.png",
                          "is_trinket": false,
                          "name": "Radiant Virtue"
                        }
                      ],
                      "kills": 3,
                      "kills_counters": {
                        "inhibitors": 0,
                        "neutral_minions": 136,
                        "neutral_minions_enemy_jungle": 15,
                        "neutral_minions_team_jungle": 89,
                        "players": 3,
                        "turrets": 0,
                        "wards": 7
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
                      "level": 15,
                      "magic_damage": {
                        "dealt": 148455,
                        "dealt_percentage": 46.63,
                        "dealt_to_champions": 13579,
                        "dealt_to_champions_percentage": 49.59,
                        "taken": 5525
                      },
                      "masteries": [],
                      "minions_killed": 155,
                      "opponent": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "physical_damage": {
                        "dealt": 20331,
                        "dealt_percentage": 5.24,
                        "dealt_to_champions": 308,
                        "dealt_to_champions_percentage": 0.72,
                        "taken": 20457
                      },
                      "player": {
                        "active": true,
                        "age": 25,
                        "birthday": "2000-11-11",
                        "first_name": "Martin",
                        "id": 31994,
                        "image_url": "https://cdn-api.pandascore.co/images/player/image/31994/kc_yike_2025_split_3.png",
                        "last_name": "Sundelin",
                        "modified_at": "2026-02-06T12:55:13Z",
                        "name": "Yike",
                        "nationality": "SE",
                        "role": "jun",
                        "slug": "yike"
                      },
                      "player_id": 31994,
                      "role": "jun",
                      "runes": [],
                      "runes_reforged": {
                        "primary_path": {
                          "id": 2,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/d4c241153ee8a7431ecad0215bf5339e.png",
                          "keystone": {
                            "id": 65,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/13598521aebb0be68b52982d46aa1b1c.png",
                            "name": "First Strike",
                            "type": "keystone"
                          },
                          "lesser_runes": [
                            {
                              "id": 19,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/44b7c635b7abab80f429fc8d8bbf8718.png",
                              "name": "Magical Footwear",
                              "type": "slot1"
                            },
                            {
                              "id": 21,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/032d8f7fe2b24e22e8740bcca4e4d84c.png",
                              "name": "Future's Market",
                              "type": "slot2"
                            },
                            {
                              "id": 24,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/4318a1583e60c295ed978505810f0282.png",
                              "name": "Cosmic Insight",
                              "type": "slot3"
                            }
                          ],
                          "name": "Inspiration",
                          "type": "path"
                        },
                        "secondary_path": {
                          "id": 1,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/rune_path/image/346a8dc90cb18766f2dfde90672a6118.png",
                          "lesser_runes": [
                            {
                              "id": 5,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/eea2c6cd75310f68cce8a704f37cf296.png",
                              "name": "Cheap Shot",
                              "type": "slot1"
                            },
                            {
                              "id": 11,
                              "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/569a1e7d3c46d9731392616eccebdd9c.png",
                              "name": "Treasure Hunter",
                              "type": "slot3"
                            }
                          ],
                          "name": "Domination",
                          "type": "path"
                        },
                        "shards": {
                          "defense": {
                            "id": 66,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/95271ed6-8b6c-4fe2-9a41-bef3646114ea.png",
                            "name": "Health Scaling",
                            "type": "shard"
                          },
                          "flex": {
                            "id": 71,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/d3fbe34e-9cf6-4777-b6b1-acf96a352c9c.png",
                            "name": "Adaptative Force",
                            "type": "shard"
                          },
                          "offense": {
                            "id": 70,
                            "image_url": "https://cdn-api.pandascore.co/images/lol/rune_node/image/f847b627-6b53-413f-8b87-939c3dd437bb.png",
                            "name": "Ability Haste",
                            "type": "shard"
                          }
                        }
                      },
                      "spells": [
                        {
                          "id": 28,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/c4122701056f18d242c22b2c0bd35642.png",
                          "name": "Flash"
                        },
                        {
                          "id": 36,
                          "image_url": "https://cdn-api.pandascore.co/images/lol/spell/image/d79fd9cc23f23592c1085e1b5262cc70.png",
                          "name": "Smite"
                        }
                      ],
                      "team": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "total_damage": {
                        "dealt": 214259,
                        "dealt_percentage": 27.99,
                        "dealt_to_champions": 16599,
                        "dealt_to_champions_percentage": 22.59,
                        "taken": 26216
                      },
                      "total_heal": 10863,
                      "total_time_crowd_control_dealt": 664,
                      "total_units_healed": 5,
                      "true_damage": {
                        "dealt": 45473,
                        "dealt_percentage": 76.9,
                        "dealt_to_champions": 2711,
                        "dealt_to_champions_percentage": 74.99,
                        "taken": 233
                      },
                      "wards": {
                        "placed": 12,
                        "sight_wards_bought_in_game": 0,
                        "vision_wards_bought_in_game": 6
                      },
                      "wards_placed": 12
                    }
                  ],
                  "position": 1,
                  "status": "finished",
                  "teams": [
                    {
                      "atakhan_kills": null,
                      "bans": [
                        3151,
                        2991,
                        3156,
                        3248,
                        3185
                      ],
                      "baron_kills": 1,
                      "chemtech_drake_kills": 0,
                      "cloud_drake_kills": 0,
                      "color": "blue",
                      "dragon_kills": 4,
                      "elder_drake_kills": 0,
                      "first_atakhan": null,
                      "first_baron": true,
                      "first_blood": false,
                      "first_dragon": true,
                      "first_herald": false,
                      "first_inhibitor": true,
                      "first_tower": true,
                      "first_voidgrub": null,
                      "gold_earned": 56850,
                      "herald_kills": 0,
                      "hextech_drake_kills": 1,
                      "infernal_drake_kills": 1,
                      "inhibitor_kills": 1,
                      "kills": 18,
                      "mountain_drake_kills": 0,
                      "ocean_drake_kills": 2,
                      "player_ids": [
                        605,
                        871,
                        1132,
                        1718,
                        31994
                      ],
                      "team": {
                        "acronym": "G2",
                        "dark_mode_image_url": "https://cdn-api.pandascore.co/dark_images/team/dark_image/88/231px_g2_esports_2019_darkmode.png",
                        "id": 88,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/88/g2-esports.png",
                        "location": "DE",
                        "modified_at": "2026-03-08T14:48:40Z",
                        "name": "G2 Esports",
                        "slug": "g2-esports"
                      },
                      "tower_kills": 9,
                      "voidgrub_kills": null
                    },
                    {
                      "atakhan_kills": null,
                      "bans": [
                        3188,
                        3157,
                        3177,
                        3208,
                        3202
                      ],
                      "baron_kills": 0,
                      "chemtech_drake_kills": 0,
                      "cloud_drake_kills": 0,
                      "color": "red",
                      "dragon_kills": 0,
                      "elder_drake_kills": 0,
                      "first_atakhan": null,
                      "first_baron": false,
                      "first_blood": true,
                      "first_dragon": false,
                      "first_herald": true,
                      "first_inhibitor": false,
                      "first_tower": false,
                      "first_voidgrub": null,
                      "gold_earned": 46536,
                      "herald_kills": 2,
                      "hextech_drake_kills": 0,
                      "infernal_drake_kills": 0,
                      "inhibitor_kills": 0,
                      "kills": 7,
                      "mountain_drake_kills": 0,
                      "ocean_drake_kills": 0,
                      "player_ids": [
                        1429,
                        2538,
                        20300,
                        21577,
                        22950
                      ],
                      "team": {
                        "acronym": "KOI",
                        "dark_mode_image_url": null,
                        "id": 129970,
                        "image_url": "https://cdn-api.pandascore.co/images/team/image/129970/koi__28_spanish_team_29logo_square.png",
                        "location": "ES",
                        "modified_at": "2024-12-12T17:14:31Z",
                        "name": "KOI",
                        "slug": "ibai-x-pique"
                      },
                      "tower_kills": 3,
                      "voidgrub_kills": null
                    }
                  ],
                  "winner": {
                    "id": 88,
                    "type": "Team"
                  },
                  "winner_type": "Team"
                }
              },
              "Without detailed stats": {
                "description": "/lol/games/211263",
                "value": {
                  "begin_at": "2019-12-06T00:57:03Z",
                  "complete": false,
                  "detailed_stats": false,
                  "end_at": "2019-12-06T01:02:08Z",
                  "finished": true,
                  "forfeit": false,
                  "id": 211263,
                  "length": 304,
                  "match": {
                    "begin_at": "2019-12-06T00:57:03Z",
                    "detailed_stats": false,
                    "draw": false,
                    "end_at": "2019-12-06T01:02:07Z",
                    "forfeit": false,
                    "game_advantage": null,
                    "games": [
                      {
                        "begin_at": "2019-12-06T00:57:03Z",
                        "complete": false,
                        "detailed_stats": false,
                        "end_at": "2019-12-06T01:02:08Z",
                        "finished": true,
                        "forfeit": false,
                        "id": 211263,
                        "length": 304,
                        "match_id": 551614,
                        "position": 1,
                        "status": "finished",
                        "winner": {
                          "id": 126569,
                          "type": "Team"
                        },
                        "winner_type": "Team"
                      }
                    ],
                    "id": 551614,
                    "league": {
                      "id": 296,
                      "image_url": "https://cdn-api.pandascore.co/images/league/image/296/all-star_2020_logo-png",
                      "modified_at": "2024-04-17T21:24:17Z",
                      "name": "All-Star",
                      "slug": "league-of-legends-all-star",
                      "url": null
                    },
                    "league_id": 296,
                    "live": {
                      "opens_at": null,
                      "supported": false,
                      "url": null
                    },
                    "match_type": "best_of",
                    "modified_at": "2019-12-06T01:02:08Z",
                    "name": "CoreJJ vs Mikyx",
                    "number_of_games": 1,
                    "opponents": [
                      {
                        "opponent": {
                          "acronym": null,
                          "dark_mode_image_url": null,
                          "id": 126568,
                          "image_url": null,
                          "location": null,
                          "modified_at": "2019-12-04T13:05:31Z",
                          "name": "CoreJJ",
                          "slug": "corejj"
                        },
                        "type": "Team"
                      },
                      {
                        "opponent": {
                          "acronym": null,
                          "dark_mode_image_url": null,
                          "id": 126569,
                          "image_url": null,
                          "location": null,
                          "modified_at": "2019-12-04T13:05:39Z",
                          "name": "Mikyx",
                          "slug": "mikyx"
                        },
                        "type": "Team"
                      }
                    ],
                    "original_scheduled_at": "2019-12-06T01:00:00Z",
                    "rescheduled": false,
                    "results": [
                      {
                        "score": 0,
                        "team_id": 126568
                      },
                      {
                        "score": 1,
                        "team_id": 126569
                      }
                    ],
                    "scheduled_at": "2019-12-06T01:00:00Z",
                    "serie": {
                      "begin_at": "2019-12-04T23:00:00Z",
                      "end_at": "2019-12-06T23:00:00Z",
                      "full_name": "2019",
                      "id": 2191,
                      "league_id": 296,
                      "modified_at": "2019-11-20T15:34:41Z",
                      "name": null,
                      "season": null,
                      "slug": "league-of-legends-all-star-2019",
                      "winner_id": null,
                      "winner_type": null,
                      "year": 2019
                    },
                    "serie_id": 2191,
                    "slug": "corejj-vs-mikyx-2019-12-06",
                    "status": "finished",
                    "streams_list": [],
                    "tournament": {
                      "begin_at": "2019-12-06T01:00:00Z",
                      "country": null,
                      "detailed_stats": false,
                      "end_at": "2019-12-08T06:00:00Z",
                      "has_bracket": true,
                      "id": 3416,
                      "league_id": 296,
                      "live_supported": false,
                      "modified_at": "2020-06-17T06:24:29Z",
                      "name": "AllStar one vs one",
                      "prizepool": null,
                      "region": null,
                      "serie_id": 2191,
                      "slug": "league-of-legends-all-star-2019-one-vs-one",
                      "tier": null,
                      "type": null,
                      "winner_id": null,
                      "winner_type": "Team"
                    },
                    "tournament_id": 3416,
                    "videogame": {
                      "id": 1,
                      "name": "LoL",
                      "slug": "league-of-legends"
                    },
                    "videogame_version": null,
                    "winner": {
                      "acronym": null,
                      "dark_mode_image_url": null,
                      "id": 126569,
                      "image_url": null,
                      "location": null,
                      "modified_at": "2019-12-04T13:05:39Z",
                      "name": "Mikyx",
                      "slug": "mikyx"
                    },
                    "winner_id": 126569,
                    "winner_type": "Team"
                  },
                  "match_id": 551614,
                  "players": null,
                  "position": 1,
                  "status": "finished",
                  "teams": null,
                  "winner": {
                    "id": 126569,
                    "type": "Team"
                  },
                  "winner_type": "Team"
                }
              }
            },
            "schema": {
              "$ref": "#/components/schemas/LoLGame"
            }
          }
        },
        "description": "A League-of-Legends game\n\nDeprecated fields:\n- players[].minions_killed\n"
      }
    },
    "schemas": {
      "LoLGame": {
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
          "match": {
            "additionalProperties": false,
            "deprecated": false,
            "description": "A match",
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
              "videogame_version",
              "winner",
              "winner_id",
              "winner_type"
            ],
            "title": "FullGameMatch",
            "type": "object"
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
                "cs_diff_at_14": {
                  "deprecated": false,
                  "description": "Player CS difference compared to their lane opponent at the 14th minute in-game",
                  "nullable": true,
                  "title": "LolCreepScoreDifferenceAt14",
                  "type": "number"
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
                    "dealt_percentage": {
                      "deprecated": false,
                      "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                      "maximum": 100,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLPlayerDamageDealtPercentage",
                      "type": "number"
                    },
                    "dealt_to_champions": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
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
                      "title": "LoLDamage",
                      "type": "integer"
                    }
                  },
                  "required": [
                    "dealt",
                    "dealt_percentage",
                    "dealt_to_champions",
                    "dealt_to_champions_percentage",
                    "taken"
                  ],
                  "title": "LoLMagicDamage",
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
                    "dealt_percentage": {
                      "deprecated": false,
                      "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                      "maximum": 100,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLPlayerDamageDealtPercentage",
                      "type": "number"
                    },
                    "dealt_to_champions": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
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
                      "title": "LoLDamage",
                      "type": "integer"
                    }
                  },
                  "required": [
                    "dealt",
                    "dealt_percentage",
                    "dealt_to_champions",
                    "dealt_to_champions_percentage",
                    "taken"
                  ],
                  "title": "LoLPhysicalDamage",
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
                    "dealt_percentage": {
                      "deprecated": false,
                      "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                      "maximum": 100,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLPlayerDamageDealtPercentage",
                      "type": "number"
                    },
                    "dealt_to_champions": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
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
                      "title": "LoLDamage",
                      "type": "integer"
                    }
                  },
                  "required": [
                    "dealt",
                    "dealt_percentage",
                    "dealt_to_champions",
                    "dealt_to_champions_percentage",
                    "taken"
                  ],
                  "title": "LoLTotalDamage",
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
                    "dealt_percentage": {
                      "deprecated": false,
                      "description": "Percentage of damage dealt the player had compared to the total damage of the team",
                      "maximum": 100,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLPlayerDamageDealtPercentage",
                      "type": "number"
                    },
                    "dealt_to_champions": {
                      "deprecated": false,
                      "minimum": 0,
                      "nullable": true,
                      "title": "LoLDamage",
                      "type": "integer"
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
                      "title": "LoLDamage",
                      "type": "integer"
                    }
                  },
                  "required": [
                    "dealt",
                    "dealt_percentage",
                    "dealt_to_champions",
                    "dealt_to_champions_percentage",
                    "taken"
                  ],
                  "title": "LoLTrueDamage",
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
                "cs_diff_at_14",
                "deaths",
                "flags",
                "game_id",
                "gold_earned",
                "gold_percentage",
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
              "title": "LoLGamePlayer",
              "type": "object"
            },
            "nullable": true,
            "title": "LoLGamePlayers",
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
          "teams": {
            "deprecated": false,
            "items": {
              "additionalProperties": false,
              "deprecated": false,
              "description": "Team's data for a Game",
              "properties": {
                "atakhan_kills": {
                  "deprecated": false,
                  "description": "The number of Atakhan killed by a team.",
                  "maximum": 1,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLAtakhanKills",
                  "type": "integer"
                },
                "bans": {
                  "items": {
                    "minimum": 1,
                    "title": "LoLChampionID",
                    "type": "integer"
                  },
                  "title": "LoLChampionIDs",
                  "type": "array"
                },
                "baron_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLBaronKills",
                  "type": "integer"
                },
                "chemtech_drake_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLChemtechDrakeKills",
                  "type": "integer"
                },
                "cloud_drake_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLCloudDrakeKills",
                  "type": "integer"
                },
                "color": {
                  "enum": [
                    "blue",
                    "red"
                  ],
                  "title": "LoLTeamColor",
                  "type": "string"
                },
                "dragon_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLDragonKills",
                  "type": "integer"
                },
                "elder_drake_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLElderDrakeKills",
                  "type": "integer"
                },
                "first_atakhan": {
                  "deprecated": false,
                  "description": "Whether team killed the first Atakhan",
                  "nullable": true,
                  "title": "LoLTeamGotFirstAtakhan",
                  "type": "boolean"
                },
                "first_baron": {
                  "deprecated": false,
                  "description": "Whether team got first baron Nashor",
                  "nullable": true,
                  "title": "LoLTeamGotFirstBaron",
                  "type": "boolean"
                },
                "first_blood": {
                  "deprecated": false,
                  "description": "Whether team got first blood",
                  "nullable": true,
                  "title": "LoLTeamGotFirstBlood",
                  "type": "boolean"
                },
                "first_dragon": {
                  "deprecated": false,
                  "description": "Whether team got first dragon",
                  "nullable": true,
                  "title": "LoLTeamGotFirstDragon",
                  "type": "boolean"
                },
                "first_herald": {
                  "deprecated": false,
                  "description": "Whether team got first herald",
                  "nullable": true,
                  "title": "LoLTeamGotFirstHerald",
                  "type": "boolean"
                },
                "first_inhibitor": {
                  "deprecated": false,
                  "description": "Whether team got first inhibitor",
                  "nullable": true,
                  "title": "LoLTeamGotFirstInhibitor",
                  "type": "boolean"
                },
                "first_tower": {
                  "deprecated": false,
                  "description": "Whether team got first tower",
                  "nullable": true,
                  "title": "LoLTeamGotFirstTower",
                  "type": "boolean"
                },
                "first_voidgrub": {
                  "deprecated": false,
                  "description": "Whether team killed the first voidgrub",
                  "nullable": true,
                  "title": "LoLTeamGotFirstVoidgrub",
                  "type": "boolean"
                },
                "gold_earned": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLGold",
                  "type": "integer"
                },
                "herald_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLHeraldKills",
                  "type": "integer"
                },
                "hextech_drake_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLHextechDrakeKills",
                  "type": "integer"
                },
                "infernal_drake_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLInfernalDrakeKills",
                  "type": "integer"
                },
                "inhibitor_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLInhibitorKills",
                  "type": "integer"
                },
                "kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLKillCount",
                  "type": "integer"
                },
                "mountain_drake_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLMountainDrakeKills",
                  "type": "integer"
                },
                "ocean_drake_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLOceanDrakeKills",
                  "type": "integer"
                },
                "player_ids": {
                  "items": {
                    "description": "ID of the player",
                    "minimum": 1,
                    "title": "PlayerID",
                    "type": "integer"
                  },
                  "title": "PlayerIDs",
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
                "tower_kills": {
                  "deprecated": false,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLTowerKills",
                  "type": "integer"
                },
                "voidgrub_kills": {
                  "deprecated": false,
                  "description": "The number of voidgrubs killed by a team.",
                  "maximum": 6,
                  "minimum": 0,
                  "nullable": true,
                  "title": "LoLVoidgrubKills",
                  "type": "integer"
                }
              },
              "required": [
                "atakhan_kills",
                "bans",
                "baron_kills",
                "chemtech_drake_kills",
                "cloud_drake_kills",
                "color",
                "dragon_kills",
                "elder_drake_kills",
                "first_atakhan",
                "first_baron",
                "first_blood",
                "first_dragon",
                "first_herald",
                "first_inhibitor",
                "first_tower",
                "first_voidgrub",
                "gold_earned",
                "herald_kills",
                "hextech_drake_kills",
                "infernal_drake_kills",
                "inhibitor_kills",
                "kills",
                "mountain_drake_kills",
                "ocean_drake_kills",
                "player_ids",
                "team",
                "tower_kills",
                "voidgrub_kills"
              ],
              "title": "LoLGameTeam",
              "type": "object"
            },
            "nullable": true,
            "title": "LoLGameTeams",
            "type": "array"
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
          "match",
          "match_id",
          "players",
          "position",
          "status",
          "teams",
          "winner",
          "winner_type"
        ],
        "title": "LoLGame",
        "type": "object"
      },
      "LoLGameID": {
        "description": "LoL game ID",
        "minimum": 1,
        "title": "LoLGameID",
        "type": "integer"
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
    "/lol/games/{lol_game_id}": {
      "get": {
        "description": "Get a single League of Legends game by ID\n> ℹ️  \n> \n> This endpoint is only available to customers with a historical or real-time data plan",
        "operationId": "get_lol_games_lolGameId",
        "parameters": [
          {
            "description": "A LoL game ID",
            "in": "path",
            "name": "lol_game_id",
            "required": true,
            "schema": {
              "$ref": "#/components/schemas/LoLGameID"
            }
          }
        ],
        "responses": {
          "200": {
            "$ref": "#/components/responses/LoLGame"
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
        "summary": "Get a game",
        "tags": [
          "LoL games"
        ],
        "x-pandascore-plan": "Historical plan",
        "x-readme": {
          "code-samples": [
            {
              "code": "curl --request GET \\\n     --url 'https://api.pandascore.co/lol/games/{lol_game_id}' \\\n     --header 'accept: application/json'\n",
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