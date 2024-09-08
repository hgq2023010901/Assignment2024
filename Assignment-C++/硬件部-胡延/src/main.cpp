#include <iostream>
#include <fstream>
#include <nlohmann/json.hpp>
#include <curl/curl.h>

// 使用 nlohmann/json 的命名空间
using json = nlohmann::json;

// libcurl 写入数据的回调函数
static size_t WriteCallback(void *contents, size_t size, size_t nmemb, void *userp) {
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

int main() {
    // 读取 config.json
    std::ifstream InputFile("config.json");
    json config;
    InputFile >> config;

    // 验证 config.json 是否存在
    if(!InputFile.is_open()) {
        std::cerr << "config.json not found" << std::endl;
        return 1;
    }

    // 获取网址并初始化 libcurl
    std::string url = config["url"];
    CURL *curl;
    CURLcode res;
    std::string readBuffer;

    curl = curl_easy_init();
    if(curl) {
        // 设置网址、写入回调函数、写入数据的目标并执行 HTTP 请求
        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer)
        res = curl_easy_perform(curl);
        // 检查是否有错误发生
        if(res != CURLE_OK) {
            std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
        }
        // 重置 libcurl
        curl_easy_cleanup(curl);

        // 将网页内容保存到文件
        std::ofstream outfile("page.html");
        outfile << readBuffer;
        outfile.close();
    }

    return 0;
}
