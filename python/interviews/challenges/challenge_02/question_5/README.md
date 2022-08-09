## Question 5
Package your code into a container and deploy it to a container registry of your choice.
   
## Solution
Note, requires login to docker.
1. Go to repository root directory.
2. Build Docker image:
   - `docker build . -t challenge02-image -f question_5/Dockerfile`
3. Tag image:
   - `docker tag challenge02-image dockerusername/challenge02-image:v1`
4. Push image:
   - `docker push dockerusername/challenge02-image:v1`

### Test
1. Pull image:
   - `docker pull dockerusername/challenge02-image:v1`
2. Run image:
   - `docker run -p 8080:8080 -it dockerusername/challenge02-image:v1`
3. Same testing process as described in question_3
