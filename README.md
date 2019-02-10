# adinet-api
Public facing API for personal projects; such as a build detection microservice, trello tracker, and health logger; accessible via https://api.adi.wtf/ 🎊

### Environment Setup
An environment is setup based on a ``.env`` file utilizing [python-dotenv](https://github.com/theskumar/python-dotenv)

# Endpoints

## Discord™ Endpoint
The Discord™ endpoint is utilized in projects such https://gh.adi.wtf/build-bot and https://gh.adi.wtf/dfetch.

This is intended to track the current build number for the Discord canary, ptb, and stable release channels.

| **Channel**   | **Description**                                | **Endpoint**     |
| ------------- |:-----------------------------------------------|:-----------------|
| Canary        | Fastest release channel, meant for bug hunting | /discord/canary/ |
| PTB           | More stable, paired with more early features   | /discord/ptb/    |
| Stable        | The intended platform for users                | /discord/stable/ |


### Builds
A build is a JSON-object returned by the endpoints described below, they look like so:
```json
{
  "build_id": "BUILD_ID",
  "build_hash": "BUILD_HASH",
  "build_num": "BUILD_NUM",
  "build_rel_time": "BUILD_REL_TIME"
}
```

``BUILD_HASH`` - a 40 long alphaneumeric string which can be used for identification and differentiation between builds, these are unique.
``BUILD_ID`` - a 7 long alphaneumeric string that is the first **7** characters of ``BUILD_HASH``.
``BUILD_NUM`` - a numerical integer referring to the current build number of Discord clients for *that* release channel, ascends over time.
``BUILD_REL_TIME`` - when the build was observed by the tracking microservice.

#### ``/``
Returns every known, tracked build (since the existence of the [build tracker](https://gh.adi.wtf/dfetch)) in a JSON serializable array ``[]`` which contains ``n`` number builds.

#### ``/latest/``
Returns the single highest build, returned by seeking the highest build available in the known list of builds.

#### ``/<build_num>``
Returns the build matching the number given, can be useful for finding when the build was released, on top of many other purposes.
