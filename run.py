#!/usr/bin/env python3
"""
ApplyPilot AI - Server Launcher
Usage: python run.py
"""
import os
import sys
import uvicorn

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("DEBUG", "True").lower() in ("true", "1")
    
    print("=" * 65)
    print("Starting ApplyPilot AI Server...")
    print(f"Web SaaS Dashboard:   http://{host}:{port}/")
    print(f"Interactive API Docs: http://{host}:{port}/docs")
    print(f"WhatsApp Webhook:     http://{host}:{port}/api/whatsapp/webhook")
    print("=" * 65)
    
    uvicorn.run("app.main:app", host=host, port=port, reload=reload)
