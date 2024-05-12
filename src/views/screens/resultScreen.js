import { View, Text } from "react-native";
import { useRoute } from "@react-navigation/native";
import React from "react";

const ResultScreen = ({ navigation }) => {
  const route = useRoute();
  const {
    address,
    name,
    type,
    bedrooms,
    bathrooms,
    size,
    age,
    tenure,
    units,
    district,
    amenities,
    price
  } = route.params;
  console.log(price);

  return <View>
    <Text>Address: {address}</Text>
      <Text>Name: {name}</Text>
      <Text>Tenure: {tenure}</Text>
      <Text>Price: {price}</Text>
  </View>;
};
export default ResultScreen;
