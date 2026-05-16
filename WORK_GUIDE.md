# Working guide

This guide guides you through every contributor's responsibilities and architecture clues.

___

## Architecture

Please follow these definitions so you don't mess up everything

### Tree

```
src/
├── main.py              # Entry point — instantiates the QApplication subclass and starts the app
├── core/
│   ├── database.py      # Database connection and setup
│   └── config.py        # App-wide configuration
├── models/              # Data models
├── repositories/        # SQL abstraction layer — all raw queries live here
├── services/            # Business logic
├── viewmodels/          # Bridges services and UI
└── ui/
    ├── controllers/     # UI controllers
    ├── shared/          # Shared UI utilities and components
    ├── widgets/         # Reusable, ready-made components for controllers
    └── app.py           # QApplication subclass — do not run directly
```

### Layer responsibilities

- core — infrastructure only; no business logic 
- models — pure data structures; no logic, no DB calls 
- repositories — the only place that talks to the database; always go through here, never query directly from services or UI 
- services — business logic; depends on repositories, never on UI 
- viewmodels — translate service data into something the UI can bind to directly 
- ui — strictly presentation; no business logic, no direct DB access 

### Notes

- app.py holds the QApplication subclass. main.py imports and runs it — don't add startup logic anywhere else. 
- ui/shared/ is the right place for anything reused across the UI layer. 

___

## What not to do

1. Don't create catch-all folders like helpers/ or utils/. If code doesn't have a clear home, that's a sign it belongs in an existing layer — move it there. Catch-all folders grow fast and become impossible to maintain.
2. Don't bypass the repository layer. Services and UI must never query the database directly. All DB access goes through repositories/ — that's the whole point of having it.
3. Don't put business logic in the UI. Controllers and widgets handle presentation only. If you're writing conditions or data transformations inside a controller, it belongs in a service or viewmodel instead.
4. Don't put logic in models. Models are plain data structures. No DB calls, no business rules, no formatting.
5. Don't add new files to a layer without understanding what that layer is for. Read this guide first. If you're unsure where something goes, ask before creating a new file.
6. Don't add startup logic outside of main.py. App initialization lives in one place.
7. Don't do large commits across several file, be more concrete when commiting, the content of the commit should be clear through the commit message.

___

# Contributor responsibilities

The project is divided into three layers, each owned by one contributor. The team leader oversees all layers, resolves conflicts, and handles integration. \

1. davidnot13 — Data layer:
    - Owns: core/, models/, repositories/
    - Responsible for the database setup, schema, all queries, and data models. Nothing above this layer should touch the DB.
2. Eusain1 — Logic layer
    - Owns: services/, viewmodels/
    - Responsible for all business logic and the translation of data into UI-ready structures. Depends on **Data Layer work** — coordinate on model changes.
3. black4736251 — UI layer
    - Owns: ui/ (controllers/, widgets/, shared/)
    - Responsible for all visual components and user interaction. No logic, no DB calls — if you need data processed, ask the responsible for **Logic Layer**.
4. Team leader
    - Owns: main.py, ui/app.py, overall architecture
    - Reviews all cross-layer changes, settles any disputes about where code belongs.

___

# Q&A

___

### If you have any questions, ask them, and they'll be answered here.