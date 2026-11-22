
import asyncio

from app.database import repository


async def get_students_async():
    return await asyncio.to_thread(repository.get_students)


async def get_faculty_async():
    return await asyncio.to_thread(repository.get_faculty)


async def get_courses_async():
    return await asyncio.to_thread(repository.get_courses)


async def get_enrollments_async():
    return await asyncio.to_thread(repository.get_enrollments)


async def get_all_data_async():
    results = await asyncio.gather(
        get_students_async(),
        get_faculty_async(),
        get_courses_async(),
        get_enrollments_async()
    )

    return {
        "students": results[0],
        "faculty": results[1],
        "courses": results[2],
        "enrollments": results[3]
    }


if __name__ == "__main__":
    data = asyncio.run(get_all_data_async())

    for module, records in data.items():
        print(f"{module}: {len(records)} records")
