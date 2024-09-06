-- Define the project
set_project("my_project")
set_version("1.0.0")
add_requires("nlohmann_json")
add_requires("libcurl")

-- Define the target (executable)
target("my_project")
    set_kind("binary")
    add_files("src/*.cpp")  -- Source files in the src/ directory
    add_includedirs("include")  -- Header files in the include/ directory
    add_packages("nlohmann_json", "libcurl", "cpr")
