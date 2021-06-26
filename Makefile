
build: ## Build the application
	docker-compose -f docker-compose.yaml build

clean: ## Stop and remove containers
	docker-compose -f docker-compose.yaml down -v --remove-orphan

up: ## Start the containers and main application
	docker-compose -f docker-compose.yaml up
