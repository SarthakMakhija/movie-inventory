# movie-inventory
A repository containing first python + flask (practice) project.

# Problem definition

*MMasters* (a hypothetical company) is a movie inventory company and they wish to introduce new features in their system.

Hello,

We are an "API first" company providing a lot of APIs around movie snapshots. We would like to introduce few features in the system -

We wish to pull movies from OMDB (http://www.omdbapi.com/) and store in our system as movie snapshots.

We would also like to allow anyone to retrieve these movie snapshots.

As mentioned, we are an "API first" company and we now expect to build two APIs -
- one that *gets all movie snapshots* from our system
    - is an OPEN API
- one that *creates movie snapshots* in our system by fetching the information from omdb
    - is a protected API
    - every request should contain a header "x-api-key" with "d2ViLWFwcGxpY2F0aW9uLWluLWZsYXNr" as the value
    - allow our people to pass mutiple movie titles to be fetched from OMDB

We expect proper **REST status** in the system - 
- 500 for INTERNAL_SERVER_ERROR
- 200 for OK
- 201 for CREATED
- 401 for UNAUTHORIZED
...and so on

Movie snapshot includes - 
- title
- release year
- release date
- director
- and ratings which is a collection

**Summarizing**

As a part of the system
- build APIs
- ensure security
- fetch from OMDB
- store in the system
- get all movie snapshots from the system
- include retries while communicating with OMDB
- and needless to say, ensure that the system is properly tested

# Pairing by
- [Abhijeet Sonawane](https://github.com/abhijeetsonawane)
- [Sarthak Makhija](https://github.com/SarthakMakhija)

# Run tests
- pipenv shell
- python3 run_tests.py all
