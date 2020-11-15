


dpl ?= deploy.env
include $(dpl)
export $(shell sed 's/=.*//' $(dpl))

# DOCKER TASKS
# Build the container
build: ## Build the container
	docker build -t $(APP_NAME) .



run: ## Build the container
	docker-compose up --build

	
	