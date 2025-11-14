const country_code: Record<string, string> = {
  India: "0091",
  Australia: "0025",
  Nepal: "00977"
};

function print(text: string) {
  return text;
}

function getCode(country: string) {
  return country_code[country] ?? "Not Found";
}

print("Country code for India -");
print(getCode("India"));

print("Country code for Japan -");
print(getCode("Japan"));

print("Country code for Nepal -");
print(getCode("Nepal"));
