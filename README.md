# MicroFlask
Demo of using Flask back end micro services loosely decoupled within docker containers.

To install:

1. Clone the project
    ```bash
    git clone https://github.com/jmeisele/MicroFlask.git
    ```
2. Change directories into the repo
    ```bash
    cd MicroFlask
    ```
3. Run docker compose
    ```bash
    docker-compose up
    ```
4. Send an order to the order service
    ```bash
    curl http://localhost:3001?params
    ```

# TODOs
- [X] Construct docker compose file to get all services up and running
- [ ] Create additional delivery microservice using NodeJS

If you found this repo helpful, a [small donation](https://www.buymeacoffee.com/VlduzAG) would be greatly appreciated. 
All proceeds go towards coffee, and all coffee goes towards more code.
