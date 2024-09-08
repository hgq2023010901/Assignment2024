#include <iostream>
#include <fstream>
#include <curl/curl.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

// 定义一个回调函数来处理接收到的数据
size_t WriteCallback(void *ptr, size_t size, size_t nmemb, void *data) {
    auto *str = static_cast<std::string *>(data);
    str->append(static_cast<char*>(ptr), size * nmemb);
    return size * nmemb;
}

bool downloadWebPage(const std::string& url, const std::string& filename) {
    CURL *curl;
    CURLcode res;
    std::string readBuffer;

    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L); // 允许重定向
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

        res = curl_easy_perform(curl);

        if (res != CURLE_OK) {
            std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
            return false;
        }

        // 关闭curl句柄
        curl_easy_cleanup(curl);

        // 将数据写入文件
        std::ofstream file(filename);
        if (file.is_open()) {
            file << readBuffer;
            file.close();
            return true;
        } else {
            std::cerr << "Failed to open file for writing." << std::endl;
            return false;
        }
    } else {
        std::cerr << "Failed to initialize curl." << std::endl;
        return false;
    }
}

int main() {
    // 读取JSON文件
    std::ifstream config_file("config.json");
    if (!config_file.is_open()) {
        std::cerr << "Failed to open config.json" << std::endl;
        return 1;
    }
    json config;
    try {
        config_file >> config;
        config_file.close();
    } catch (const std::exception& e) {
        std::cerr << "Error parsing JSON: " << e.what() << std::endl;
        return 1;
    }

    // 获取URL并下载网页
    if (config.contains("url")) {
        std::string url = config["url"];
        if (downloadWebPage(url, "webpage.html")) {
            std::cout << "Web page saved as webpage.html" << std::endl;
        } else {
            std::cerr << "Failed to download web page." << std::endl;
        }
    } else {
        std::cerr << "URL not found in config.json" << std::endl;
    }

    return 0;
}