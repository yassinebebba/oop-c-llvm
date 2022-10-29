class String {
    char * first_name;
    char * last_name;
    int age;
    void __init__(String *self, char* first_name, char * last_name, int age) {
        self->first_name = first_name;
        self->last_name = last_name;
        self->age = age;
    }
    int getAge(String *self) {
        return self->age;
    }
}
int main() {
    String * string = new String("Malte", "Ressin", 41);
    String *secondString = new String("Yassine", "Bebba", 23);
    printf("Hi my name is %s %s and I am %d years old.\n", string->first_name, string->last_name, string->getAge());
    printf("Hi my name is %s %s and I am %d years old.\n", secondString->first_name, secondString->last_name, secondString->age);
    free(string);
    free(secondString);
    return 0;
}