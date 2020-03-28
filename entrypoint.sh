#!/bin/bash
gunicorn app:app --bind=:$PORT