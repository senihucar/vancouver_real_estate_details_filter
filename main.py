# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import assignment2

if __name__ == '__main__':
    assignment2.open_and_write_txt_file('\\\\\search by city and bedroom number (Vancouver,3)\\\\\\\ \n')
    assignment2.search_by_city_and_bedroom_number('Vancouver', 3)
    assignment2.open_and_write_txt_file('\n\\\\\search by price range(550000,1000000 )\\\\\\\ \n')
    assignment2.search_by_price_range(550000, 1000000)
    assignment2.open_and_write_txt_file('\n\\\\\search by city and property type(Burnaby,House)\\\\\\\ \n')
    assignment2.search_by_city_and_property_type('Burnaby', 'House')
    assignment2.open_and_write_txt_file('\n\\\\\ reduce price\\\\\\\ \n')
    assignment2.reduce_price()
    assignment2.open_and_write_txt_file('\n\\\\\search_by_postal_code_range(V,7)\\\\\\\ \n')
    assignment2.search_by_postal_code_range('V', '7')
    assignment2.open_and_write_txt_file('\n\\\\\Details of the MLS : R2508895 : are\\\\\\\ \n')
    assignment2.get_listing('R2508895')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
