def deploy_app():
    print("Starting deployment")

    build_status = "success"

    if build_status == "success":
        print("Build passed")
        print("Deploying application...")
    else:
        print("Build failed")
        print("Stopping pipeline")


def run_tests():
    print("Running tests...")
    tests_passed = True

    if tests_passed:
        print("All tests passed")
    else:
        print("Tests failed")


def main():
    run_tests()
    deploy_app()


if __name__ == "__main__":
    main()
