def main():
    from apps import OnboardingAPI

    from infra.in_memory_repositories \
        import \
        InMemorySoftwareRepository, \
        InMemoryClientRepository, \
        InMemoryPermissionRepository

    software_repo = InMemorySoftwareRepository()
    client_repo = InMemoryClientRepository()
    permission_repo = InMemoryPermissionRepository()

    app = OnboardingAPI(5003, software_repo, client_repo, permission_repo)
    app.run()


if __name__ == "__main__":
    main()
