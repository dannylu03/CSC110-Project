from entities.QuarterlyShipping import QuarterlyShipping


# Static variables maps month to quarter
QUARTERS = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 3, 10: 4, 11: 4, 12: 4}


def quarterly_shipping_sort(to_be_sorted: [QuarterlyShipping]) -> None:
    for i in range(len(to_be_sorted)):
        earliest = i
        for j in range(i+1, len(to_be_sorted)):
            if to_be_sorted[i].year > to_be_sorted[j].year:
                earliest = j
            elif to_be_sorted[i].year == to_be_sorted[j].year and to_be_sorted[i].quarter > to_be_sorted[j].quarter:
                earliest = j
        to_be_sorted[i], to_be_sorted[earliest] = to_be_sorted[earliest], to_be_sorted[i]
