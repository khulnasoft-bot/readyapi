# Projektgenerierung – Vorlage

Sie können einen Projektgenerator für den Einstieg verwenden, welcher einen Großteil der Ersteinrichtung, Sicherheit, Datenbank und einige API-Endpunkte bereits für Sie erstellt.

Ein Projektgenerator verfügt immer über ein sehr spezifisches Setup, das Sie aktualisieren und an Ihre eigenen Bedürfnisse anpassen sollten, aber es könnte ein guter Ausgangspunkt für Ihr Projekt sein.

## Full Stack ReadyAPI PostgreSQL

GitHub: <a href="https://github.com/khulnasoft/full-stack-readyapi-postgresql" class="external-link" target="_blank">https://github.com/khulnasoft/full-stack-readyapi-postgresql</a>

### Full Stack ReadyAPI PostgreSQL – Funktionen

* Vollständige **Docker**-Integration (Docker-basiert).
* Docker-Schwarmmodus-Deployment.
* **Docker Compose**-Integration und Optimierung für die lokale Entwicklung.
* **Produktionsbereit** Python-Webserver, verwendet Uvicorn und Gunicorn.
* Python <a href="https://github.com/khulnasoft/readyapi" class="external-link" target="_blank">**ReadyAPI**</a>-Backend:
    * **Schnell**: Sehr hohe Leistung, auf Augenhöhe mit **NodeJS** und **Go** (dank Starlette und Pydantic).
    * **Intuitiv**: Hervorragende Editor-Unterstützung. <abbr title="Auch bekannt als automatische Vervollständigung, IntelliSense">Codevervollständigung</abbr> überall. Weniger Zeitaufwand für das Debuggen.
    * **Einfach**: Einfach zu bedienen und zu erlernen. Weniger Zeit für das Lesen von Dokumentationen.
    * **Kurz**: Codeverdoppelung minimieren. Mehrere Funktionalitäten aus jeder Parameterdeklaration.
    * **Robust**: Erhalten Sie produktionsbereiten Code. Mit automatischer, interaktiver Dokumentation.
    * **Standards-basiert**: Basierend auf (und vollständig kompatibel mit) den offenen Standards für APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> und <a href="https://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.
    * <a href="https://readyapi.github.io/features/" class="external-link" target="_blank">**Viele weitere Funktionen**</a>, einschließlich automatischer Validierung, Serialisierung, interaktiver Dokumentation, Authentifizierung mit OAuth2-JWT-Tokens, usw.
* **Sicheres Passwort**-Hashing standardmäßig.
* **JWT-Token**-Authentifizierung.
* **SQLAlchemy**-Modelle (unabhängig von Flask-Erweiterungen, sodass sie direkt mit Celery-Workern verwendet werden können).
* Grundlegende Startmodelle für Benutzer (ändern und entfernen Sie nach Bedarf).
* **Alembic**-Migrationen.
* **CORS** (Cross Origin Resource Sharing).
* **Celery**-Worker, welche Modelle und Code aus dem Rest des Backends selektiv importieren und verwenden können.
* REST-Backend-Tests basierend auf **Pytest**, integriert in Docker, sodass Sie die vollständige API-Interaktion unabhängig von der Datenbank testen können. Da es in Docker ausgeführt wird, kann jedes Mal ein neuer Datenspeicher von Grund auf erstellt werden (Sie können also ElasticSearch, MongoDB, CouchDB oder was auch immer Sie möchten verwenden und einfach testen, ob die API funktioniert).
* Einfache Python-Integration mit **Jupyter-Kerneln** für Remote- oder In-Docker-Entwicklung mit Erweiterungen wie Atom Hydrogen oder Visual Studio Code Jupyter.
* **Vue**-Frontend:
    * Mit Vue CLI generiert.
    * Handhabung der **JWT-Authentifizierung**.
    * Login-View.
    * Nach der Anmeldung Hauptansicht des Dashboards.
    * Haupt-Dashboard mit Benutzererstellung und -bearbeitung.
    * Bearbeitung des eigenen Benutzers.
    * **Vuex**.
    * **Vue-Router**.
    * **Vuetify** für schöne Material-Designkomponenten.
    * **TypeScript**.
    * Docker-Server basierend auf **Nginx** (konfiguriert, um gut mit Vue-Router zu funktionieren).
    * Mehrstufigen Docker-Erstellung, sodass Sie kompilierten Code nicht speichern oder committen müssen.
    * Frontend-Tests, welche zur Erstellungszeit ausgeführt werden (können auch deaktiviert werden).
    * So modular wie möglich gestaltet, sodass es sofort einsatzbereit ist. Sie können es aber mit Vue CLI neu generieren oder es so wie Sie möchten erstellen und wiederverwenden, was Sie möchten.
* **PGAdmin** für die PostgreSQL-Datenbank, können Sie problemlos ändern, sodass PHPMyAdmin und MySQL verwendet wird.
* **Flower** für die Überwachung von Celery-Jobs.
* Load Balancing zwischen Frontend und Backend mit **Traefik**, sodass Sie beide unter derselben Domain haben können, getrennt durch den Pfad, aber von unterschiedlichen Containern ausgeliefert.
* Traefik-Integration, einschließlich automatischer Generierung von Let's Encrypt-**HTTPS**-Zertifikaten.
* GitLab **CI** (kontinuierliche Integration), einschließlich Frontend- und Backend-Testen.

## Full Stack ReadyAPI Couchbase

GitHub: <a href="https://github.com/khulnasoft/full-stack-readyapi-couchbase" class="external-link" target="_blank">https://github.com/khulnasoft/full-stack-readyapi-couchbase</a>

⚠️ **WARNUNG** ⚠️

Wenn Sie ein neues Projekt von Grund auf starten, prüfen Sie die Alternativen hier.

Zum Beispiel könnte der Projektgenerator <a href="https://github.com/khulnasoft/full-stack-readyapi-postgresql" class="external-link" target="_blank">Full Stack ReadyAPI PostgreSQL</a> eine bessere Alternative sein, da er aktiv gepflegt und genutzt wird. Und er enthält alle neuen Funktionen und Verbesserungen.

Es steht Ihnen weiterhin frei, den Couchbase-basierten Generator zu verwenden, wenn Sie möchten. Er sollte wahrscheinlich immer noch gut funktionieren, und wenn Sie bereits ein Projekt damit erstellt haben, ist das auch in Ordnung (und Sie haben es wahrscheinlich bereits an Ihre Bedürfnisse angepasst).

Weitere Informationen hierzu finden Sie in der Dokumentation des Repos.

## Full Stack ReadyAPI MongoDB

... könnte später kommen, abhängig von meiner verfügbaren Zeit und anderen Faktoren. 😅 🎉

## Modelle für maschinelles Lernen mit spaCy und ReadyAPI

GitHub: <a href="https://github.com/microsoft/cookiecutter-spacy-readyapi" class="external-link" target="_blank">https://github.com/microsoft/cookiecutter-spacy-readyapi</a>

### Modelle für maschinelles Lernen mit spaCy und ReadyAPI – Funktionen

* **spaCy** NER-Modellintegration.
* **Azure Cognitive Search**-Anforderungsformat integriert.
* **Produktionsbereit** Python-Webserver, verwendet Uvicorn und Gunicorn.
* **Azure DevOps** Kubernetes (AKS) CI/CD-Deployment integriert.
* **Mehrsprachig** Wählen Sie bei der Projekteinrichtung ganz einfach eine der integrierten Sprachen von spaCy aus.
* **Einfach erweiterbar** auf andere Modellframeworks (Pytorch, Tensorflow), nicht nur auf SpaCy.
