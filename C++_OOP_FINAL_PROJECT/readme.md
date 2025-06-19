
 HERE ARE DETAILED NOTE ABOUT MY PROJECT
 
The task assigned was to develop an Insurance Quote System using C++ that demonstrates object-oriented programming principles such as abstraction, inheritance, and polymorphism. The system needed to support the creation of multiple quote engines (such as basic and premium types), manage age-based rate brackets dynamically, and provide premium quotations based on the applicant's age and policy type. It also required a user interface for interacting with the system through a console-based menu.
To achieve this, two data structures were defined: Applicant and RateBracket. The Applicant structure stores information such as vehicle identification number (VIN), age, and policy type. The RateBracket structure holds minimum and maximum age values along with the corresponding premium rate. These structures serve as the foundation for storing and processing applicant and rate data.
At the core of the system is the abstract base class QuoteEngine, which manages a dynamic array of RateBracket entries and includes common functionality like adding, removing, listing, and searching brackets. It also declares a pure virtual function named calculate(), which is overridden in the derived classes. The findPremium() helper function, defined within the base class, is used to locate the correct premium based on an applicant's age by scanning through the stored brackets.
Two derived classes extend the functionality of QuoteEngine. The BasicEngine calculates premiums directly based on the matching rate bracket without any modification. On the other hand, the PremiumEngine introduces a 50% surcharge by multiplying the base premium by 1.5, representing a more expensive policy type.
User interaction is handled via a text-based menu loop in the main() function. Upon launching the program, the user specifies how many engines to create and the type of each engine (basic or premium). The menu allows the user to add rate brackets, remove them by index, list all brackets for a specific engine, quote an applicant by entering their information, or search for brackets within a given age range. For each applicant, the program prints a premium quote for each engine created. If no matching bracket is found for the applicant’s age, an appropriate message is displayed.
Helper functions such as displayMenu(), promptEngineIndex(), and clearInputBuffer() assist with input validation and improving the user experience. Dynamic memory is used throughout the system for managing engine and bracket storage, and memory is properly cleaned up before the program terminates.
In conclusion, the code successfully demonstrates key object-oriented programming concepts by using abstract classes, virtual functions, inheritance, and dynamic memory. It provides a flexible, extensible structure for managing insurance quotes based on different engine behaviors and user-defined rate brackets. This system can be easily extended further with features like file I/O, GUI integration, or more advanced pricing rules if needed.


BLOCK OF CODE WITH THE COMMENT LINE FOR EVERY LINE 

#include <iostream>  // For input/output stream functions like cout, cin
#include <cstring>   // For string handling functions like strcpy, strcmp
#include <limits>    // For clearing input buffer using numeric limits

using namespace std; // Use the standard namespace to avoid writing std:: everywhere

// -------------------------- STRUCT DEFINITIONS --------------------------

// Structure to store applicant's information
struct Applicant {
    char vin[17];   // Vehicle Identification Number (16 characters max + '\0')
    int age;        // Applicant's age
    char type[10];  // Policy type name (e.g., "basic" or "premium")
};

// Structure to represent a premium rate bracket
struct RateBracket {
    float minAge;   // Minimum age of this bracket
    float maxAge;   // Maximum age of this bracket
    float premium;  // Premium amount for this age range
};

// -------------------------- ABSTRACT BASE CLASS --------------------------

// Abstract base class representing the insurance quote engine
class QuoteEngine {
protected:
    RateBracket* brackets; // Dynamically allocated array of RateBrackets
    int size;              // Number of rate brackets

public:
    // Constructor: initializes with no brackets
    QuoteEngine() : brackets(nullptr), size(0) {}

    // Destructor: cleans up dynamically allocated brackets
    virtual ~QuoteEngine() {
        delete[] brackets;
    }

    // Pure virtual function to calculate premium - to be overridden by derived classes
    virtual float calculate(const Applicant* applicant) = 0;

    // Adds a new bracket to the list
    void addBracket(const RateBracket& rb) {
        // Create a new array one element larger
        RateBracket* newBrackets = new RateBracket[size + 1];
        // Copy old brackets to new array
        for (int i = 0; i < size; ++i)
            newBrackets[i] = brackets[i];
        // Add the new bracket at the end
        newBrackets[size] = rb;
        // Delete old bracket array and replace with new one
        delete[] brackets;
        brackets = newBrackets;
        ++size; // Increase count
    }

    // Removes a bracket at a specific index
    void removeBracket(int index) {
        // Invalid index check
        if (index < 0 || index >= size) return;
        // Create a new array one element smaller
        RateBracket* newBrackets = new RateBracket[size - 1];
        // Copy all except the one to be removed
        for (int i = 0, j = 0; i < size; ++i) {
            if (i != index)
                newBrackets[j++] = brackets[i];
        }
        delete[] brackets;
        brackets = newBrackets;
        --size; // Decrease count
    }

    // Displays all stored rate brackets
    void listBrackets() const {
        if (size == 0) {
            cout << "No rate brackets available.\n";
            return;
        }
        for (int i = 0; i < size; ++i) {
            cout << "Bracket #" << i << ": Age " << brackets[i].minAge << "-" << brackets[i].maxAge
                 << ", Premium = " << brackets[i].premium << "\n";
        }
    }

    // Searches and displays brackets within a given age range
    void searchBracket(float minAge, float maxAge) const {
        bool found = false;
        for (int i = 0; i < size; ++i) {
            if (brackets[i].minAge >= minAge && brackets[i].maxAge <= maxAge) {
                cout << "Bracket #" << i << ": Age " << brackets[i].minAge << "-" << brackets[i].maxAge
                     << ", Premium = " << brackets[i].premium << "\n";
                found = true;
            }
        }
        if (!found)
            cout << "No matching brackets found in range.\n";
    }

protected:
    // Helper function to find the premium based on applicant's age
    float findPremium(int age) {
        for (int i = 0; i < size; ++i) {
            if ((brackets + i)->minAge <= age && age <= (brackets + i)->maxAge)
                return (brackets + i)->premium;
        }
        return -1.0f; // Return -1 if no match is found
    }
};

// -------------------------- DERIVED CLASSES --------------------------

// BasicEngine simply returns the base premium found
class BasicEngine : public QuoteEngine {
public:
    float calculate(const Applicant* applicant) override {
        return findPremium(applicant->age); // No surcharge
    }
};

// PremiumEngine applies a 50% surcharge to the base premium
class PremiumEngine : public QuoteEngine {
public:
    float calculate(const Applicant* applicant) override {
        float base = findPremium(applicant->age);
        return base < 0 ? -1 : base * 1.5f; // 50% increase
    }
};

// -------------------------- HELPER FUNCTIONS --------------------------

// Clears the input buffer to prevent unwanted characters in next input
void clearInputBuffer() {
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

// Prompts user to select an engine index
void promptEngineIndex(int engineCount) {
    cout << "Select engine index";
    if (engineCount == 1) {
        cout << ": 0\n"; // Only one engine
    } else {
        cout << " from: ";
        for (int i = 0; i < engineCount; ++i) {
            cout << i;
            if (i != engineCount - 1) cout << ", ";
        }
        cout << "\n";
    }
}

// Displays the main system menu
void displayMenu() {
    cout << "\n--- Insurance Quote System Menu ---\n";
    cout << "1. Add Rate Bracket to Engine\n";
    cout << "2. Remove Rate Bracket from Engine\n";
    cout << "3. List All Brackets for Engine\n";
    cout << "4. Quote an Applicant\n";
    cout << "5. Search Bracket Range\n";
    cout << "6. Exit\n";
    cout << "Enter your choice: ";
}

// -------------------------- MAIN FUNCTION --------------------------

int main() {
    int engineCount;
    cout << "Enter number of engines you want to create: ";
    cin >> engineCount;

    // Dynamically allocate an array of pointers to QuoteEngine
    QuoteEngine** engines = new QuoteEngine*[engineCount];

    // Let user choose type for each engine
    for (int i = 0; i < engineCount; ++i) {
        int choice;
        cout << "Select type for engine #" << i + 1 << " (1 = Basic, 2 = Premium): ";
        cin >> choice;
        // Create the chosen engine type
        engines[i] = (choice == 1) ? static_cast<QuoteEngine*>(new BasicEngine())
                                   : static_cast<QuoteEngine*>(new PremiumEngine());
    }

    bool running = true; // Main loop flag
    while (running) {
        displayMenu();    // Show options
        int option;
        cin >> option;    // Get user's choice

        switch (option) {
        case 1: { // Add bracket
            int engineIndex;
            RateBracket rb;
            promptEngineIndex(engineCount); // Prompt user to choose engine
            cin >> engineIndex;
            cout << "Enter minAge: ";
            cin >> rb.minAge;
            cout << "Enter maxAge: ";
            cin >> rb.maxAge;
            cout << "Enter premium: ";
            cin >> rb.premium;

            if (engineIndex >= 0 && engineIndex < engineCount) {
                engines[engineIndex]->addBracket(rb); // Add bracket to selected engine
                cout << "Bracket added! Current brackets for Engine #" << engineIndex << ":\n";
                engines[engineIndex]->listBrackets();
            } else {
                cout << "Invalid engine index.\n";
            }
            break;
        }
        case 2: { // Remove bracket
            int engineIndex, bracketIndex;
            promptEngineIndex(engineCount);
            cin >> engineIndex;
            cout << "Enter index of bracket to remove: ";
            cin >> bracketIndex;

            if (engineIndex >= 0 && engineIndex < engineCount) {
                engines[engineIndex]->removeBracket(bracketIndex);
                cout << "Bracket removed! Current brackets for Engine #" << engineIndex << ":\n";
                engines[engineIndex]->listBrackets();
            } else {
                cout << "Invalid engine index.\n";
            }
            break;
        }
        case 3: { // List all brackets
            int engineIndex;
            promptEngineIndex(engineCount);
            cin >> engineIndex;

            if (engineIndex >= 0 && engineIndex < engineCount) {
                engines[engineIndex]->listBrackets();
            } else {
                cout << "Invalid engine index.\n";
            }
            break;
        }
        case 4: { // Quote applicant
            Applicant app;
            cout << "Enter VIN (max 16 characters): ";
            clearInputBuffer();       // Clear input buffer before getline
            cin.getline(app.vin, 17); // Read VIN
            cout << "Enter Age: ";
            cin >> app.age;
            cout << "Enter Policy Type: ";
            clearInputBuffer();
            cin.getline(app.type, 10); // Read policy type

            cout << "--- Quotes ---\n";
            for (int i = 0; i < engineCount; ++i) {
                float premium = engines[i]->calculate(&app);
                if (premium < 0)
                    cout << "Engine #" << i << ": No matching rate bracket found.\n";
                else
                    cout << "Engine #" << i << ": Premium = " << premium << " RWF\n";
            }
            break;
        }
        case 5: { // Search bracket range
            int engineIndex;
            float minAge, maxAge;
            promptEngineIndex(engineCount);
            cin >> engineIndex;

            if (engineIndex >= 0 && engineIndex < engineCount) {
                cout << "Enter search minimum age: ";
                cin >> minAge;
                cout << "Enter search maximum age: ";
                cin >> maxAge;
                engines[engineIndex]->searchBracket(minAge, maxAge);
            } else {
                cout << "Invalid engine index.\n";
            }
            break;
        }
        case 6:
            running = false; // Exit the loop
            break;
        default:
            cout << "Invalid option.\n"; // Handle invalid input
        }
    }

    // Free all dynamically allocated memory
    for (int i = 0; i < engineCount; ++i)
        delete engines[i];  // Delete each engine
    delete[] engines;       // Delete the array itself

    return 0; // End of program
}
![Screenshot 2025-06-18 153524](https://github.com/user-attachments/assets/fa171a5e-b56e-46ae-b23c-4fe94af9abcd)
![Screenshot 2025-06-18 153417](https://github.com/user-attachments/assets/55dee72c-67d7-4191-a441-daf6795f365e)
![Screenshot 2025-06-18 153226](https://github.com/user-attachments/assets/a7cd636b-9aca-47a2-bbd4-da5bdc9a2f25)
![Screenshot 2025-06-18 153158](https://github.com/user-attachments/assets/727a23cc-7ea7-45f4-847e-631e4d380f4f)
![Screenshot 2025-06-18 153016](https://github.com/user-attachments/assets/6ffc2100-81f2-4d8d-a852-d2c17e99086d)
![Screenshot 2025-06-18 152920](https://github.com/user-attachments/assets/e54b38f0-062e-4190-a0d5-b94675b32ef6)

![Screenshot 2025-06-18 152046](https://github.com/user-attachments/assets/cfe1fba4-b999-4e27-890b-ffd4ccb3ae04)
![Screenshot 2025-06-18 152128](https://github.com/user-attachments/assets/a50d6e2d-e095-44b6-90a3-b6ba868f6341)
![Screenshot 2025-06-18 152257](https://github.com/user-attachments/assets/ce2c77b5-14bf-4584-af43-46fdae06ee34)
![Screenshot 2025-06-18 152753](https://github.com/user-attachments/assets/f3e0c000-6731-489c-a8e6-8c0873339407)

![Screenshot 2025-06-18 140905](https://github.com/user-attachments/assets/a79d852a-d1f3-4ac9-a13e-4056650c976d)
![Screenshot 2025-06-18 142455](https://github.com/user-attachments/assets/ba7602e8-c6f9-48ef-ae3d-78464b9b1730)
![Screenshot 2025-06-18 142601](https://github.com/user-attachments/assets/fbff3828-7fde-47fc-a925-91ca51246457)





