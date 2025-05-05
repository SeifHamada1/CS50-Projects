#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *forensic = fopen(argv[1], "r");
    if (forensic == NULL)
    {
        printf("File was not found\n");
        return 1;
    }

    FILE *currentFile = NULL;
    int jpegCount = 0; // Start counting from 0
    char *filename = malloc(8 * sizeof(char));
    if (filename == NULL)
    {
        fclose(forensic);
        printf("Memory allocation error\n");
        return 1;
    }

    BYTE buffer[512];
    while (fread(buffer, sizeof(BYTE), 512, forensic) == 512) // Using sizeof(BYTE) for clarity
    {
        // Check for matching 4 bytes, indicating start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // If file exists, close it before starting a new one
            if (currentFile != NULL)
            {
                fclose(currentFile);
            }

            sprintf(filename, "%03i.jpg", jpegCount);
            currentFile = fopen(filename, "w");

            if (currentFile == NULL)
            {
                free(filename);
                fclose(forensic);
                printf("Error creating file\n");
                return 1;
            }

            jpegCount++;
        }

        // If file exists, write to it
        if (currentFile != NULL)
        {
            fwrite(buffer, sizeof(BYTE), 512, currentFile); // Write using the original buffer
        }
    }

    // Close any open files
    if (currentFile != NULL)
    {
        fclose(currentFile);
    }

    fclose(forensic);
    free(filename);

    return 0;
}
