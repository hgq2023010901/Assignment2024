add_requires("nlohmann_json")
add_requires("libcurl")

target("download_webpage")
    set_kind("binary")
    add_files("src/*.cpp")
    set_languages("c++17")
    add_packages("nlohmann_json", "libcurl")
