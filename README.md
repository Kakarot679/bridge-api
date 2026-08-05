# BridgeAPI

BridgeAPI is an API integration platform built with FastAPI and PostgreSQL.

The goal of this project is to build a backend platform that allows organizations to connect external services, manage API integrations, map data between different providers, and automate data synchronization.

This project is inspired by modern integration platforms such as Zoho Flow, Workato, and Zapier, while being built from scratch as a learning project focused on backend engineering and system design.

## Current Features

- FastAPI
- PostgreSQL
- SQLAlchemy 2.0 ORM
- Alembic Database Migrations
- Organization Management
- User Management
- Provider Management
- Connection Management

## Tech Stack

- Python
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Alembic
- Docker

## Project Status

🚧 Currently under active development.

Upcoming features include:

- API Endpoints
- Schema Mapping
- AI-assisted Field Mapping
- JWT Authentication
- Background Jobs
- Docker Deployment
- API Documentation

## Getting Started

```bash
git clone https://github.com/<your-username>/bridge-api.git

cd bridge-api

pip install -r requirements.txt

docker compose up -d

uvicorn app.main:app --reload