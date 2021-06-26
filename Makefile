
build: ## Build the application
	docker build -t nickumia/quote-scraper:latest quotes

clean: ## Stop and remove containers
	docker-compose -f docker-compose.yaml down -v --remove-orphan

up: ## Start the containers and main application
	docker-compose -f docker-compose.yaml up
