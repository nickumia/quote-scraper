
build: ## Build the application
	docker build -t nickumia/quote-server:latest quotes
	docker build -t nickumia/mail-server:latest mail
	docker build -t nickumia/scheduler:latest scheduler

clean: ## Stop and remove containers
	docker-compose -f docker-compose.yaml down -v --remove-orphan

up: ## Start the containers and main application
	docker-compose -f docker-compose.yaml up
