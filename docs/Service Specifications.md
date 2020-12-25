# Service Specifications

## Accounts Microservice

Each registered user should have the following data associated:

  + Username 
  + Email
  + Karma

The following operations have to be exposed:

  + Create user
  + Update email
  + Increment Karma
  + Decrement Karma
  + Deactivate account

The data for the user can be in the same database or different database as the other services.

## Posts Microservice

Each post should have the following data associated:

  + Title
  + Text
  + Community (subreddit)
  + **Optional**: URL linking to a resource (e.g. a news article or picture), a username, and date the post was made.

The following operations have to be exposed:

  + Create a new post
  + Delete an existing post
  + Retrieve an existing post
  + List the *n* most recent posts to a particular community
  + List the *n* most recent posts to any community

**NOTE**: When retrieving lists of posts, do not include the text or resource URL for the post.

## Votes Microservice

Each post maintained by the posting microservice can be voted up or down. This service should maintain the number of upvotes and downvotes for each post. A post’s score can be computed by subtracting the number of downvotes from the number of upvotes.

Each vote should have the following data associated:

  + Upvote
  + Downvote

The following operations should be exposed:

  + Upvote a post
  + Downvote a post
  + Report the number of upvotes and downvotes for a post
  + List the n top-scoring posts to any community
  + Given a list of post identifiers, return the list sorted by score.

**NOTE**:
  + Each upvote or downvote should include a unique identifier (e.g., a URL or database key) for the post that can be used to match votes with the posts maintained by the posting microservice
  + If this service is implemented with a database separate from the posting microservice, it is not responsible for verifying the existence of a post before recording or reporting votes

## Messages Microservice

Users can send and receive messages to each other. 

Every messages will have the following data associated with it:

  + Message ID
  + User from
  + User to
  + Message timestamp
  + Message contents
  + Message flag

The following operations will be exposed:
  + Send message
  + Delete message
  + Favorite message

Messaging data can be in the same database as other services or a separate one.
