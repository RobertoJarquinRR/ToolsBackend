"""Funciones futuras en desarrollo (pruebas iniciales)."""

import asyncio
from playwright.async_api import async_playwright
from config import credenciales


"""
async def obtener_tareas():
    # Usamos async_playwright para que sea compatible con Telegram
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless= True) 
        page = await browser.new_page()

        await page.goto(credenciales.UCN_SCRAPER_URL)

        await page.fill('#username', credenciales.USUARIO_UCN)
        await page.fill('#password', credenciales.CONTRASENA_UCN)
        await page.click("#loginbtn")

        await page.wait_for_load_state("networkidle")


        # Esperar a que carguen las tareas
        await page.wait_for_selector('[data-region="event-list-item"]')
        tareas = await page.locator('[data-region="event-list-item"]').all()

        lista_final = []

        for tarea in tareas:
            nombre = await tarea.locator(".event-name").inner_text()
            curso = await tarea.locator(".text-muted").first.inner_text()
            
            # Guardamos la info en una lista de texto
            lista_final.append(f{nombre} | Curso: {curso}")
            print(f"Tarea extraída: {nombre}")

        await browser.close()
        return lista_final  # Devolvemos la lista para que main.py la use"""