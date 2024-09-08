add_rules("mode.debug", "mode.release")
add_requires("nlohmann_json", "libcurl")

target("cpp-project-template")
    add_includedirs("src")
    set_exceptions("cxx")
    set_kind("binary")
    set_languages("cxx20")
    set_warnings("allextra")
    add_files("src/*.cpp")
    add_packages("nlohmann_json", "libcurl")

