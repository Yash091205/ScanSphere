export default function ReviewGallery({ pages }) {

    return (

        <div className="grid md:grid-cols-2 gap-6">

            {pages.map(page => (

                <div
                    key={page.id}
                    className="bg-white rounded-2xl shadow-md p-4"
                >

                    <img
                        src={`http://127.0.0.1:8000${page.preview_url}`}
                        alt={page.original_name}
                        className="rounded-xl"
                    />

                    <p className="mt-3 font-semibold">

                        {page.original_name}

                    </p>

                </div>

            ))}

        </div>

    );

}